from django.urls import path,include
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name="home")
]
