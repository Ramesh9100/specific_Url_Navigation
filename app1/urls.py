from app1.views import *

from django.urls import path

app_name='edookati'

urlpatterns=[

    path('college/',college,name='college')
]