from django.urls import path
from app1.views import *
app_name='chithra'
urlpatterns=[
    path('sai/',sai,name='sai'),
    path('chithra/',chithra,name='chithra'),
]

