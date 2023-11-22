from app2.views import *

from django.urls import path

app_name='something'

urlpatterns=[

    path('response/',response,name='response'),
]