from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=False,read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        # fields = [
        #     'product_name',
        #     'slug',
        #     'description',
        #     'price',
        #     'stock',
        #     'category'
        # ]
