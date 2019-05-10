from django.urls import path, include, re_path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^transcribe/$', views.transcribe, name='transcribe'),
]