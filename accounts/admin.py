from django.contrib import admin
from accounts.models import Profile, Follower, User


admin.site.register(Follower)
admin.site.register(Profile)
admin.site.register(User)
