from rest_api import views as rest_views
from django.urls import path


app_name = 'rest_api'

urlpatterns = [
    path('read', rest_views.readDb, name='read'),
    path('change', rest_views.changeImage, name='change'),
    path('check',rest_views.checkUsername, name='check'),
    path('getMap',rest_views.getMap, name='getMap'),
    path('getImage',rest_views.getHomeImages, name='getImage'),
    path('recommend',rest_views.recommendMenu, name='recommend'),
]
