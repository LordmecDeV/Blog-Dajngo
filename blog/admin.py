from django.contrib import admin
from blog.models import Blog
# Register your models here.

class ListContent(admin.ModelAdmin):
    list_display = ("id","nome","legenda")

admin.site.register(Blog, ListContent)