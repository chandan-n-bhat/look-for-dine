from django.urls import path
from home import views as home_views

app_name = 'home'

urlpatterns = [
    path('', home_views.homePage, name='home'),
]
