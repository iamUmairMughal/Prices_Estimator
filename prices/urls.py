from django.urls import path
from .views import *
urlpatterns = [
    path('car/', car_price, name='Cars')
]