from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

















# from rest_framework import serializers
# from datetime import datetime
#
# class Product:
#     def __init__(self, inn_code, name, description, price, quantity, date_created, expiry_date, brand, category, warehouse, user, supplier):
#         self.inn_code = inn_code
#         self.name = name
#         self.description = description
#         self.price = price
#         self.quantity = quantity
#         self.date_created = date_created or datetime.now()
#         self.expiry_date = expiry_date or datetime.now()
#         self.brand = brand
#         self.category = category
#         self.warehouse = warehouse
#         self.user = user
#         self.supplier = supplier
#
# product = Product(inn_code='12345', name='Product Name', description='Product Description', \
#                   price=100, quantity=1, brand='test', category='test', warehouse='test', \
#                   user='test', supplier='test')
#
# class ProductSerializer(serializers.Serializer):
#     inn_code = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.IntegerField()
#     quantity = serializers.IntegerField()
#     date_created = serializers.DateTimeField()
#     expiry_date = serializers.DateTimeField()
#     brand = serializers.CharField()
#     category = serializers.CharField()
#     warehouse = serializers.CharField()
#     user = serializers.CharField()
#     supplier = serializers.CharField()
#
#     def create(self, validated_data):
#         # inn_code = validated_data['inn_code']
#         # name = validated_data['name']
#         # description = validated_data['description']
#         # price = validated_data['price']
#         # quantity = validated_data['quantity']
#         # date_created = validated_data['date_created']
#         # expiry_date = validated_data['expiry_date']
#         # brand = validated_data['brand']
#         # category = validated_data['category']
#         # warehouse = validated_data['warehouse']
#         # user = validated_data['user']
#         # supplier = validated_data['supplier']
#         return Product(**validated_data)
#
#
#     def update(self, instance, validated_data):
#         instance.inn_code = validated_data.get('inn_code', instance.inn_code)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.date_created = validated_data.get('date_created', instance.date_created)
#         instance.expiry_date = validated_data.get('expiry_date', instance.expiry_date)
#         instance.brand = validated_data.get('brand', instance.brand)
#         instance.category = validated_data.get('category', instance.category)
#         instance.warehouse = validated_data.get('warehouse', instance.warehouse)
#         instance.user = validated_data.get('user', instance.user)
#         instance.supplier = validated_data.get('supplier', instance.supplier)
#         instance.save()
#         return instance


