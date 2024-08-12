from django.urls import path
from produtos.views import BrandCreateListView, BrandRetrieveUpdateDestroyView, ProductsCreateListView, ProductsRetrieveUpdateDestroyView

app_name = 'produtos'
urlpatterns = [
    path('brands', BrandCreateListView.as_view(), name='brands-create-list'),
    path('brands/<int:pk>/', BrandRetrieveUpdateDestroyView.as_view(), name='brands-detail-view'),

    path('products', ProductsCreateListView.as_view(), name='products-creat-list'),
    path('products/<int:pk>', ProductsRetrieveUpdateDestroyView.as_view(), name='products-detail-view')
] 
