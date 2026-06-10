from django.urls import path

from . import views



urlpatterns = [
    path('',views.nike,name='nike'),
    path('kharid/<int:id>/',views.kharid,name='kharid'),
    path('home_kharid/<int:id>/',views.home_kharid,name='home_kharid')
    
    
]