from django.db import models
from django.contrib.auth.models import AbstractUser


# USER MODEL
class User(AbstractUser):
    ROLE_CHOICES = (
        ('startup', 'Startup Owner'),
        ('investor', 'Investor'),
        ('mentor', 'Mentor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='startup')
    bio = models.TextField(blank=True, default='')
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)


# STARTUP MODEL
class Startup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    business_model = models.TextField(blank=True, default='')
    industry = models.CharField(max_length=100, blank=True, default='General')
    website = models.URLField(blank=True, default='')
    logo = models.ImageField(upload_to='startup_logos/', blank=True, null=True)

    market_potential = models.FloatField(default=0)
    scalability = models.FloatField(default=0)
    traction = models.FloatField(default=0)

    rating = models.FloatField(default=0)

    def calculate_rating(self):
        return round(
            (
                (self.market_potential or 0) +
                (self.scalability or 0) +
                (self.traction or 0)
            ) / 3,
            1
        )

    def save(self, *args, **kwargs):
        self.rating = self.calculate_rating()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# MENTOR MODEL
class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    bio = models.TextField(blank=True, default='')
    expertise = models.CharField(max_length=200, blank=True, default='')
    photo = models.ImageField(upload_to='mentor_photos/', blank=True, null=True)  # NEW

    def __str__(self):
        return self.user.username


# INVESTOR MODEL
class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    investment_range = models.CharField(max_length=100, default='Not specified')
    bio = models.TextField(blank=True, default='')
    focus_areas = models.CharField(max_length=200, blank=True, default='')
    photo = models.ImageField(upload_to='investor_photos/', blank=True, null=True)  # NEW

    def __str__(self):
        return self.user.username


# FEEDBACK MODEL
class Feedback(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='feedbacks')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks_given')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mentor.username} -> {self.startup.name}"


# CONNECTION REQUEST MODEL
class ConnectionRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected'),
        ],
        default='pending'
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'receiver')

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.status})"


# CHAT ROOM MODEL
class ChatRoom(models.Model):
    participants = models.ManyToManyField(User, related_name='chatrooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatRoom {self.id}"


# MESSAGE MODEL
class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:30]}"
