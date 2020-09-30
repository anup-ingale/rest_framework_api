from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.data),
]