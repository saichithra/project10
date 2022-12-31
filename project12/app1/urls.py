from django.urls import path
from app1.views import *
app_name='sai'
urlpatterns=[
    path('ntr/',ntr,name='ntr'),
]