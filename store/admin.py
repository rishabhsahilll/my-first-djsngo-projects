from django.contrib import admin
from .models import UserDta,  UserProfile

# Register your models here.
admin.site.register(UserDta)
admin.site.register(UserProfile)