from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='store_home_url'),
]
