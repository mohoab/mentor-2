from django.contrib import admin
from .models import service


class adminservices(admin.ModelAdmin):
    list_display = ['title' , 'content' , 'status']
    list_filter = ['status']
    search_fields = ['title']
    fields = ['title', 'content' , ' status']



admin.site.register(service,adminservices)
