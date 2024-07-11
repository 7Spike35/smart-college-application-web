from django.urls import path
from . import views

urlpatterns = [
    path('questionpage/', views.question, name='questions'),
]
