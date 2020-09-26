from django.urls import path
from .views import index, ItemList, ItemDetail, add_to_cart, remove_from_cart

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('hikester', index, name='index'),
    path('products', ItemList.as_view(), name='products'),
    path('product/<slug>/', ItemDetail.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),

    # path('product_details', product_details, name='product_details')
]
