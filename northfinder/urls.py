from django.urls import path
from . import views

urlpatterns = [
    path('', views.findNorth   , name ='home'),
    path('start', views.start  , name='start'),
    path('stop' , views.stop   , name='stop'),
]