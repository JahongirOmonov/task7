from django.urls import path
from .views import getstakan, poststakan, detail

urlpatterns=[
    path('all/', getstakan),
    path('detail/<int:realid>', detail),
    path('create/', poststakan)
]