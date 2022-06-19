from django.urls import path
from . import views

app_name = 'Admin'

urlpatterns = [
    path('hello/',views.Hello,name='Hello')
]