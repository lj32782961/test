from django.urls import path
from . import views

app_name = 'aichat'

urlpatterns = [
    path('', views.index, name='index'),#http://127.0.0.1:8000/index/。如果path('', views.index, name='index')，http://127.0.0.1:8000/即可
    
]


