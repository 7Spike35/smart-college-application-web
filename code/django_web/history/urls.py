from django.urls import path

from .views import history

urlpatterns=[
    path('history/', history,name='history')
]