from django.urls import path
from cars.views import *

urlpatterns = [
    path('',home,name="home"),
    path('cars/',car,name='cars'),
    path('space/',space,name='space'),
    path('park/',park,name='park'),
]
