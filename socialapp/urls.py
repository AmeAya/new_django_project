from django.urls import path
from .views import *


urlpatterns = [
    path('cabinet', cabinetView, name='cabinet_url'),
    path('test', testView, name='test_url'),
]
