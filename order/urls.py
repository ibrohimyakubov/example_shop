from django.urls import path

from order import views

urlpatterns = [
    path('shop-cart/', views.shopcart, name='shopcart')
]
