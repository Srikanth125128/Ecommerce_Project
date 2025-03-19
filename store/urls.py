from django.urls import path
from . import api_views
from .views import product_list, animal_list
from store.postman_views import product_api

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('animals/', animal_list, name='animal_list'),


    path('api/products/create/', api_views.ProductCreateView.as_view(), name="product_create"),
    path('api/products/list/', api_views.ProductListView.as_view(), name="product_list"),


    path("api/products/", product_api, name="postman_product_create"),
    path("api/products/<int:product_id>/", product_api, name="postman_product_update"),

path("api/products/<int:product_id>/", product_api, name="postman_product_delete"),
]



