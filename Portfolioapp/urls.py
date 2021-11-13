from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('download/', views.download,name='download'),
    path('downloadalbum', views.downloadalbum,name='downloadalbum'),
    path('sendmail/', views.sendmail,name='sendmail'),
    
]
