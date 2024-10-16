from django.contrib import admin
from .models import Profile,post,comments

admin.site.register(Profile)
admin.site.register(post)
admin.site.register(comments)