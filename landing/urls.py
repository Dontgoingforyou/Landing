from django.urls import path
from . import views
from .apps import LandingConfig

app_name = LandingConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_order, name='submit_order'),
    path('thank-you/', views.thank_you, name='thank_you'),
]