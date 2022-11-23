from django.urls import path

from stores.views import StoresView, StoreView, ProductView, ProductsView, CreateStoreView

app_name = 'Stores'

urlpatterns = [
    path('list/', StoresView.as_view()),
    path('new/', CreateStoreView.as_view()),
    path('<int:store_id>/', StoreView.as_view()),
    path('products/<int:product_id>/', ProductView.as_view()),
    path('products/all/', ProductsView.as_view()),
]
