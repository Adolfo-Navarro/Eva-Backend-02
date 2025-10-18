from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
    path('categoria/<str:categoria>/', views.categoria, name='categoria'),
]