from django.urls import path
from book.views import reserveTable, checkStatus

app_name = 'book'

urlpatterns = [
    path('reserve/', reserveTable, name='reserve'),
    path('status/', checkStatus, name='status')
]