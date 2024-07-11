from django.urls import path

import user.views



urlpatterns=[
    path('register/',user.views.register)
]