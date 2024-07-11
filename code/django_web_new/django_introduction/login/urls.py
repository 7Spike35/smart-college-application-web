from django.urls import path

import login.views

urlpatterns=[
    path('login/',login.views.login,name='login'),
]