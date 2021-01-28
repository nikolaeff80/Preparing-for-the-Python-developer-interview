from django.urls import path

from shop.product.views import index, add

app_name = 'product'

urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add'),
]

