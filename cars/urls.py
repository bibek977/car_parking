from django.urls import path
from cars.views import *

urlpatterns = [
    path('car/',car,name='car'),
    path('car/update/<str:pk>/',car_update,name='car_update'),
    path('car/delete/<str:pk>/',car_delete,name='car_delete'),
    path('space/',space,name='space'),
    path('space/update/<str:pk>/',space_update,name='space_update'),
    path('space/delete/<str:pk>/',space_delete,name='space_delete'),
    path('',park,name='home'),
    path('park/update/<str:pk>',park_update,name='park_update'),
    # path('park/delete/<str:pk>',park_delete,name='park_delete'),
    path('park/delete/<str:pk>',park_out,name='park_delete'),
    path('clear/',clear_all,name='clear_all'),
    path("my_view",my_view,name='my_view')
]
