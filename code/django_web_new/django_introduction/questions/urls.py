from django.urls import path

import questions.views

urlpatterns=[
    path('questions/',questions.views.questions,name='home')
]