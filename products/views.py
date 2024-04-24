from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Product, QRCode
from products.serializers import ProductSerializer
from users.permissions import IsAdministrator
from drf_spectacular.utils import extend_schema
import segno


@extend_schema(
    responses={200: ProductSerializer(many=True)},
    summary="Barcha mahsulotlar ro'yxati",
    description="Barcha mahsulotlar ro'yxati",
    tags=["Moddiy boyliklarga oid endpointlar"],
)
class ProductList(APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        all_products = Product.objects.all()
        serializer = self.serializer_class(all_products, many=True)
        data = {
            'success': True,
            'data': serializer.data,
        }
        return Response(data)



@extend_schema(
    responses={200: ProductSerializer(many=True)},
    summary="Id si ko'rsatilgan mahsulot",
    description="Id si ko'rsatilgan mahsulot. Bu endpointda ushbu idga tegishli QRcode generatsiya qilinadi",
    tags=["Moddiy boyliklarga oid endpointlar"],
)
class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        category = instance.category
        warehouse = instance.warehouse
        user = instance.user
        supplier = instance.supplier

        category_json = str(category)
        warehouse_json = str(warehouse)
        user_json = str(user)
        supplier_json = str(supplier)

        serializer = self.get_serializer(instance)
        data = serializer.data

        request_url = request.build_absolute_uri()
        # Generate QR code
        qr = segno.make(request_url)
        qr_svg_data = qr.svg_data_uri(scale=5)

        # Save QR code URL in the database
        qr_code = QRCode.objects.create(url=qr_svg_data)

        # Get the URL of the saved QR code
        qr_code_url = qr_code.url

        return Response({
            'success': True,
            'data': data,
            'category': category_json,
            'user_json': user_json,
            'supplier_json': supplier_json,
            'warehouse_json': warehouse_json,
            'qr_code_url': qr_code_url,
        })



@extend_schema(
    responses={200: ProductSerializer(many=True)},
    summary="Mahsulot yaratish",
    description="Mahsulot yaratish: bunda POST metodi ishlatiladi",
    tags=["Moddiy boyliklarga oid endpointlar"],
)
class ProductCreate(APIView):
    permission_classes = [IsAuthenticated, IsAdministrator]
    serializer_class = ProductSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'success': True,
                'data': serializer.data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@extend_schema(
    responses={200: ProductSerializer(many=True)},
    summary="Mahsulotga o'zgartirish kiritish",
    description="Mahsulotga o'zgartirish kiritish",
    tags=["Moddiy boyliklarga oid endpointlar"],
)
class ProductUpdate(APIView):
    permission_classes = [IsAuthenticated, IsAdministrator]
    serializer_class = ProductSerializer

    def put(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@extend_schema(
    responses={200: ProductSerializer(many=True)},
    summary="Mahsulotni o'chirib tashlash",
    description="Mahsulotni o'chirib tashlash",
    tags=["Moddiy boyliklarga oid endpointlar"],
)
class ProductDelete(APIView):
    permission_classes = [IsAuthenticated, IsAdministrator]
    serializer_class = ProductSerializer
    def delete(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        data = {
            'success': "Product has been deleted",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

