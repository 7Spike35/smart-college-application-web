from django.urls import path

import home.views

urlpatterns=[
    path('home/',home.views.home,name='home')
]