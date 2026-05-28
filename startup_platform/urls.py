from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('mentors/', views.mentors, name='mentors'),
    path('startups/', views.startups, name='startups'),
    path('about/', views.about, name='about'),

    # Startup
    path('add-startup/', views.add_startup, name='add_startup'),
    path('startup/edit/<int:startup_id>/', views.edit_startup, name='edit_startup'),
    path('startup/<int:startup_id>/', views.startup_profile, name='startup_profile'),

    # Connections  (FIX: removed duplicate paths, kept one consistent set)
    path('connect/<int:user_id>/', views.send_connection_request, name='connect'),
    path('connections/', views.connections, name='connections'),
    path('connections/<int:request_id>/<str:action>/', views.respond_connection, name='respond_connection'),

    # Chat
    path('inbox/', views.inbox, name='inbox'),
    path('chat/start/<int:user_id>/', views.start_chat, name='start_chat'),
    path('chat/<int:room_id>/', views.chat_room, name='chat_room'),
    path('chat/<int:room_id>/messages/', views.get_new_messages, name='get_new_messages'),
    path('chat/<int:room_id>/send/', views.send_message, name='send_message'),
    # Photo uploads
    path('update-mentor-photo/', views.update_mentor_photo, name='update_mentor_photo'),
    path('update-investor-photo/', views.update_investor_photo, name='update_investor_photo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)