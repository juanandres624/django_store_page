from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('product/', views.getProducts),
    path('product/create/', views.createProduct),
    path('product/<str:pk>/update/', views.updateProduct),
    path('product/<str:pk>/delete/', views.deleteProduct),
    path('product/<str:pk>/', views.getProduct),
]