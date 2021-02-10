from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/list/', views.product_list, name='product_list'),
    path('product/details/', views.product_details, name='product_details'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
]