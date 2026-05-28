from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import (
    User, Startup, Mentor, Investor,
    Feedback, ConnectionRequest,
    ChatRoom, Message
)

# ─────────────────────────────────────────────
# HOME
# ─────────────────────────────────────────────
def home(request):
    return render(request, 'Home.html', {
        'total_startups': Startup.objects.count(),
        'total_investors': Investor.objects.count(),
        'total_mentors': Mentor.objects.count(),
        'top_startups': Startup.objects.order_by('-rating')[:3],
    })


# ─────────────────────────────────────────────
# SIGNUP
# ─────────────────────────────────────────────
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email    = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm  = request.POST.get('confirm_password', '')
        role     = request.POST.get('role', 'startup')

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role
        )

        if role == 'mentor':
            Mentor.objects.create(user=user)
        elif role == 'investor':
            Investor.objects.create(user=user)
        else:
            Startup.objects.create(user=user, name=username + "'s Startup")

        login(request, user)
        return redirect('dashboard')

    return render(request, 'Signup.html')


# ─────────────────────────────────────────────
# LOGIN
# ─────────────────────────────────────────────
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)
            return redirect('dashboard')

        messages.error(request, "Invalid credentials")
        return redirect('login')

    return render(request, 'login.html')

# ─────────────────────────────────────────────
# LOGOUT
# ─────────────────────────────────────────────
def logout_view(request):
    logout(request)
    return redirect('home')


# ─────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────
@login_required
def dashboard(request):
    user = request.user

    if user.role == 'startup':
        startups = Startup.objects.filter(user=user).order_by('-id')
        return render(request, 'startupdash.html', {
            'startups': startups,
            'investors': Investor.objects.all()[:6],
            'mentors':   Mentor.objects.all()[:6],
        })

    elif user.role == 'investor':
        return render(request, 'investordash.html', {
            'startups': Startup.objects.all().order_by('-rating'),
            'investor': Investor.objects.filter(user=user).first(),
        })

    else:
        return render(request, 'mentordash.html', {
            'startups': Startup.objects.all().order_by('-rating'),
            'mentor': Mentor.objects.filter(user=user).first(),
        })


# ─────────────────────────────────────────────
# ADD STARTUP
# ─────────────────────────────────────────────
@login_required
def add_startup(request):
    if request.method == 'POST':
        # Compute market_potential from questionnaire answers (avg, max 10)
        market_size      = float(request.POST.get('market_size', 0))
        competition      = float(request.POST.get('competition', 0))
        customer_segment = float(request.POST.get('customer_segment', 0))
        market_potential = round(min((market_size + competition + customer_segment) / 3, 10), 1)

        # Compute scalability
        startup_stage = float(request.POST.get('startup_stage', 0))
        digital_scale = float(request.POST.get('digital_scale', 0))
        tech_driven   = float(request.POST.get('tech_driven', 0))
        scalability   = round(min((startup_stage + digital_scale + tech_driven) / 3, 10), 1)

        # Compute traction
        user_count = float(request.POST.get('user_count', 0))
        revenue    = float(request.POST.get('revenue', 0))
        funding    = float(request.POST.get('funding', 0))
        traction   = round(min((user_count + revenue + funding) / 3, 10), 1)

        startup = Startup(
            user=request.user,
            name=request.POST.get('name', ''),
            description=request.POST.get('description', ''),
            business_model=request.POST.get('business_model', ''),
            industry=request.POST.get('industry', 'General'),
            website=request.POST.get('website', ''),
            market_potential=market_potential,
            scalability=scalability,
            traction=traction,
        )
        if request.FILES.get('logo'):
            startup.logo = request.FILES['logo']
        startup.save()  # save() auto-calculates rating via model's save()
        messages.success(request, f"Startup created! Rating: {startup.rating}/10 ⭐")
        return redirect('dashboard')

    return render(request, 'add_startup.html')


# ─────────────────────────────────────────────
# EDIT STARTUP
# ─────────────────────────────────────────────
@login_required
def edit_startup(request, startup_id):
    s = get_object_or_404(Startup, id=startup_id, user=request.user)

    if request.method == 'POST':
        s.name           = request.POST.get('name', '')
        s.description    = request.POST.get('description', '')
        s.business_model = request.POST.get('business_model', '')
        s.industry       = request.POST.get('industry', 'General')
        s.website        = request.POST.get('website', '')

        # Compute market_potential from questionnaire (avg of 3 answers, max 10)
        market_size      = float(request.POST.get('market_size', 0))
        competition      = float(request.POST.get('competition', 0))
        customer_segment = float(request.POST.get('customer_segment', 0))
        s.market_potential = round(min((market_size + competition + customer_segment) / 3, 10), 1)

        # Compute scalability from questionnaire (avg of 3 answers, max 10)
        startup_stage  = float(request.POST.get('startup_stage', 0))
        digital_scale  = float(request.POST.get('digital_scale', 0))
        tech_driven    = float(request.POST.get('tech_driven', 0))
        s.scalability  = round(min((startup_stage + digital_scale + tech_driven) / 3, 10), 1)

        # Compute traction from questionnaire (avg of 3 answers, max 10)
        user_count  = float(request.POST.get('user_count', 0))
        revenue     = float(request.POST.get('revenue', 0))
        funding     = float(request.POST.get('funding', 0))
        s.traction  = round(min((user_count + revenue + funding) / 3, 10), 1)

        if request.FILES.get('logo'):
            s.logo = request.FILES['logo']

        s.save()  # save() auto-calculates overall rating via model's save()
        messages.success(request, f"Rating updated! Your startup scored {s.rating}/10 ⭐")
        return redirect('dashboard')

    return render(request, 'edit_startup.html', {'startup': s})


# ─────────────────────────────────────────────
# STARTUP PROFILE
# ─────────────────────────────────────────────
def startup_profile(request, startup_id):
    s = get_object_or_404(Startup, id=startup_id)
    return render(request, 'startup_profile.html', {
        'startup':   s,
        'feedbacks': s.feedbacks.all(),
    })


# ─────────────────────────────────────────────
# MENTORS
# ─────────────────────────────────────────────
def mentors(request):
    return render(request, 'Mentors.html', {
        'mentors': Mentor.objects.all()
    })


# ─────────────────────────────────────────────
# STARTUPS LIST
# ─────────────────────────────────────────────
def startups(request):
    q    = request.GET.get('q', '')
    data = Startup.objects.all()

    if q:
        data = data.filter(
            Q(name__icontains=q) |
            Q(industry__icontains=q)
        )

    return render(request, 'Startups.html', {
        'startups': data.order_by('-rating'),
        'query': q,
    })


# ─────────────────────────────────────────────
# ABOUT
# ─────────────────────────────────────────────
def about(request):
    return render(request, 'Aboutus.html')


# ─────────────────────────────────────────────
# CONNECTION SYSTEM
# ─────────────────────────────────────────────
@login_required(login_url='/login/')
def send_connection_request(request, user_id):
    receiver = get_object_or_404(User, id=user_id)

    if receiver == request.user:
        return redirect('dashboard')

    conn, created = ConnectionRequest.objects.get_or_create(
        sender=request.user,
        receiver=receiver
    )

    if not created and conn.status == 'rejected':
        conn.status = 'pending'
        conn.save()

    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))


# FIX: only ONE definition of respond_connection
@login_required(login_url='/login/')
def respond_connection(request, request_id, action):
    conn = get_object_or_404(ConnectionRequest, id=request_id, receiver=request.user)
    conn.status = 'accepted' if action == 'accept' else 'rejected'
    conn.save()
    return redirect('connections')


# FIX: use Q (already imported) instead of models.Q
@login_required(login_url='/login/')
def connections(request):
    user = request.user

    pending  = ConnectionRequest.objects.filter(receiver=user, status='pending')
    accepted = ConnectionRequest.objects.filter(status='accepted').filter(
        Q(sender=user) | Q(receiver=user)
    )

    return render(request, 'connections.html', {
        'pending':  pending,
        'accepted': accepted,
    })


# ─────────────────────────────────────────────
# CHAT SYSTEM
# ─────────────────────────────────────────────
@login_required(login_url='/login/')
def inbox(request):
    chatrooms = request.user.chatrooms.all()
    return render(request, 'inbox.html', {'chatrooms': chatrooms})


@login_required(login_url='/login/')
def start_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)

    if other_user == request.user:
        return redirect('inbox')

    chatroom = ChatRoom.objects.filter(
        participants=request.user
    ).filter(
        participants=other_user
    ).first()

    if not chatroom:
        chatroom = ChatRoom.objects.create()
        chatroom.participants.add(request.user, other_user)

    return redirect('chat_room', room_id=chatroom.id)


@login_required(login_url='/login/')
def chat_room(request, room_id):
    chatroom = get_object_or_404(ChatRoom, id=room_id, participants=request.user)
    return render(request, 'chat_room.html', {
        'chatroom':   chatroom,
        'messages':   chatroom.messages.order_by('timestamp'),
        'other_user': chatroom.participants.exclude(id=request.user.id).first(),
    })


@login_required(login_url='/login/')
@require_POST
def send_message(request, room_id):
    chatroom = get_object_or_404(ChatRoom, id=room_id, participants=request.user)
    content  = request.POST.get('content', '').strip()

    if not content:
        return JsonResponse({'error': 'Empty message'}, status=400)

    msg = Message.objects.create(
        room=chatroom,
        sender=request.user,
        content=content
    )

    return JsonResponse({
        'id':        msg.id,
        'sender':    msg.sender.username,
        'content':   msg.content,
        'timestamp': msg.timestamp.strftime('%H:%M'),
    })


@login_required(login_url='/login/')
def get_new_messages(request, room_id):
    chatroom = get_object_or_404(ChatRoom, id=room_id, participants=request.user)
    after_id = request.GET.get('after', 0)
    msgs     = chatroom.messages.filter(id__gt=after_id)

    return JsonResponse({
        'messages': [
            {
                'id':        m.id,
                'sender':    m.sender.username,
                'content':   m.content,
                'timestamp': m.timestamp.strftime('%H:%M'),
            }
            for m in msgs
        ]
    })

# ─────────────────────────────────────────────
# UPDATE MENTOR PHOTO
# ─────────────────────────────────────────────
@login_required
def update_mentor_photo(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        if photo:
            mentor = Mentor.objects.filter(user=request.user).first()
            if mentor:
                mentor.photo = photo
                mentor.save()
    return redirect('dashboard')


# ─────────────────────────────────────────────
# UPDATE INVESTOR PHOTO
# ─────────────────────────────────────────────
@login_required
def update_investor_photo(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        if photo:
            investor = Investor.objects.filter(user=request.user).first()
            if investor:
                investor.photo = photo
                investor.save()
    return redirect('dashboard')
