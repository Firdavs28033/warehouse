
from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Product, Category, Warehouse, Supplier
from users.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class WarehouseSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Warehouse
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    warehouse = WarehouseSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'













