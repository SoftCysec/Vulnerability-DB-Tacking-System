from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
