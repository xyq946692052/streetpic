from django.urls import path
from mainsite import views

urlpatterns = [
    path('', views.index),
]
