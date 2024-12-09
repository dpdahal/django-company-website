from django.db import models

# Create your models here.

class Setting(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    favicon = models.ImageField(upload_to='favicon/', blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keyword = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name