from django.contrib import admin
from .models import User, Startup, Mentor, Investor, Feedback, ConnectionRequest


admin.site.register(User)
admin.site.register(Startup)
admin.site.register(Mentor)
admin.site.register(Investor)
admin.site.register(Feedback)
admin.site.register(ConnectionRequest)