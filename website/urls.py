from django.urls import path,include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'/blog', views.BlogViewSet)



urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about, name='about-us'),
    path('service', views.service_views, name='service'),
    path('service/<slug>', views.service_details, name='service-details'),
    path('blog', views.blog_views, name='blog'),
    path('blog/<slug>', views.blog_details, name='blog-details'),
    path('contact', views.contact_view, name='contact'),
    path('api-news', views.api_news, name='api-news'),
     path('api', include(router.urls)),

]
