from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
        category = CategorySerializer(read_only = True, many=True)
        category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

        class Meta:
             model = Product
             fields = ['id', 'name', 'description', 'price', 'category', 'category_id', 'created_at']




