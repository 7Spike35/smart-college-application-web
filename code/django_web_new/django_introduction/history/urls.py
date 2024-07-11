from django.urls import path

import history.views

urlpatterns=[
    path('history/',history.views.history,name='history')
]