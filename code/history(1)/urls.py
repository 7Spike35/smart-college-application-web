from django.urls import path

from .views import history
from .views import historyinfo


urlpatterns=[
    path('history/', history,name='history'),
    path('historyinfo/', historyinfo,name='historyinfo')
]