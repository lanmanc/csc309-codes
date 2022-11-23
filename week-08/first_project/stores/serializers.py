from rest_framework import serializers

from stores.models import Store, Product


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'url', 'name', 'description', 'email']


class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()

    class Meta:
        model = Product
        fields = ['store', 'name', 'price', 'is_available']
