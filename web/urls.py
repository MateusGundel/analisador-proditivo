from django.urls import path
from web import views

urlpatterns = [
    path('', views.home_view),
    path('analisar/', views.analisar),
]