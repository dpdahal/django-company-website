from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import *

@admin.register(Setting)
class AdminSetting(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'phone', 'address']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Page)
class AdminPage(admin.ModelAdmin):
    list_display = ['title', 'slug', 'sub_title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ['title', 'slug', 'sub_title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PageChild)
class AdminPageChild(admin.ModelAdmin):
    list_display = ['page', 'title']
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
        list_display = ['name']


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['title',  'category','show_image']
    prepopulated_fields = {'slug': ('title',)}

    def show_image(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100"/>')
        return "No Image"




@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email']




    