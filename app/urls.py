from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from .views import *

app_name = 'app'

urlpatterns=[
   
    path('',Index3),
    path('index',Index1),
    path('i18n/en/',include("django.conf.urls.i18n")),
    path('i18n/ru/',include("django.conf.urls.i18n")),
    path('i18n/en/',include("django.conf.urls.i18n")),
   
    
]

# urlpatterns=[
#     path('', views.home, name='home') 
# ]