from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from stores.models import Store, Product
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# class StoresView(TemplateView):
#     template_name = 'stores/stores.html'
#
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs) | \
#                {'stores': Store.objects.all()}
from stores.serializers import StoreSerializer, ProductSerializer


class StoresView(ListView):
    template_name = 'stores/stores.html'
    queryset = Store.objects.all()
    context_object_name = 'stores'


# class StoreView(APIView):
#     def get(self, request, *args, **kwargs):
#         store = get_object_or_404(Store, id=kwargs['store_id'])
#         return Response({
#             'id': store.id,
#             'name': store.name,
#             'description': store.description,
#             'url': store.url,
#             'email': store.email
#         })

class StoreView(RetrieveAPIView, UpdateAPIView):
    serializer_class = StoreSerializer

    def get_object(self):
        return get_object_or_404(Store, id=self.kwargs['store_id'])


class CreateStoreView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreSerializer


class ProductView(RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        return get_object_or_404(Product, id=self.kwargs['product_id'])


class ProductsView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

