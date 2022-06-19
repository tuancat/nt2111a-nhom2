from django.urls import path
from . import views


app_name = 'Movie'

urlpatterns = [
    path('Movie',views.Movie)
]