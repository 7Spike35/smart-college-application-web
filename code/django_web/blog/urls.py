from django.urls import path,include

import blog.views



urlpatterns=[
    path('hello_world',blog.views.Hellow_World)
]