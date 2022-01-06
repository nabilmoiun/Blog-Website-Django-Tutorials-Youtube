from django.contrib import admin

from .models import Follow, User


admin.site.register(User)
admin.site.register(Follow)
