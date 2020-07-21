from django.urls import path,include
from . import views
from .views import post_list
app_name = "mainpage"
urlpatterns = [
    path('',post_list, name='post_list'),
]