from django.contrib import admin
from .models import post

# Register your models here.
admin.site.register(post)
class post(admin.ModelAdmin):
    list_display=['id', 'title', 'desc', 'img']


