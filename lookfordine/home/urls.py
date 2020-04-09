from django.urls import path
from home import views as home_views

app_name = 'home'

urlpatterns = [
    path('', home_views.redirectHome, name='redirectToHome'),
    path('home/', home_views.homePage, name='home'),
]
