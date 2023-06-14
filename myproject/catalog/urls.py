from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('category/<int:pk>', views.get_category_products),
    path('product/<str:name>/<int:pk>', views.get_product_products),
    path('add-product-to-cart/<int:pk>', views.add_product_to_cart),
    path('cart/', views.cart),
    path('del_item/<int:pk>', views.delete_from_cart),
    path('send_to_tg', views.complete_order)
]

