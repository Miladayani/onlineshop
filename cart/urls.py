from django.urls import path
from .views import cart_detail_view, cart_add, remove_from_cart


app_name = 'cart'
urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='add_to_cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_to_cart'),
]