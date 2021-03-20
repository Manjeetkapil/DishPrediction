# posts/admin.py
from django.contrib import admin

from .models import Post


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'foodimage')
