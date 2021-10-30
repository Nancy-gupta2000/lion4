from django.urls import path
from .views import test1api

urlpatterns = [
    path('lion/', test1api)
]
