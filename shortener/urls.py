from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index/create/', views.create),
    path('<str:pk>', views.go)
]
