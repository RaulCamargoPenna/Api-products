from rest_framework import serializers
from produtos.models import Brands, Products


class BrandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brands
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'