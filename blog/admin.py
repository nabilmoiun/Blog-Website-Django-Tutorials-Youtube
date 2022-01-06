from django.contrib import admin

from .models import *


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply)
