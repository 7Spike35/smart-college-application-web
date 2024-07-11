from django.urls import path
from . import views
import info.views





urlpatterns=[
    path('info/',info.views.info,name='info'),
    path('analy',views.analy,name='analy')
]