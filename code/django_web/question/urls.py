from django.urls import path

import question.views

urlpatterns = [
    path('questionpage/', question.views.question1, name='questionpage'),
    path('questionpage/', question.views.question2, name='questionpage')
]
