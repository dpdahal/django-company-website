from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Setting)
class AdminSetting(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'phone', 'address']
    prepopulated_fields = {'slug': ('name',)}
