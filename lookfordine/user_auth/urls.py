from django.urls import path
from user_auth import views as auth_views

app_name = 'user_auth'

urlpatterns = [
    path('login/', auth_views.customer_login, name='login'),
    path('logout/', auth_views.customer_logout, name='logout'),
    path('signup/', auth_views.signup, name='signup'),
    path('getUsers',auth_views.getUsers, name='getUsers'),
]
