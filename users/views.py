from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import UserSerializer, UserProfileSerializer, MyTokenObtainPairSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

@extend_schema(
    responses={200: UserSerializer(many=True)},
    summary="Foydalanuvchi registratsiya qilishi uchun endpoint",
    description="Registratsiya qilish",
    tags=["Avtorizatsiyaga oid endpointlar"],
)
class UserRegistrationView(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    responses={200: UserSerializer(many=True)},
    summary="User login qilishi uchun endpoint",
    description="Foydalanuvchi login qilishi uchun endpoint.",
    tags=["Avtorizatsiyaga oid endpointlar"],
    )
class UserLoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@extend_schema(
    responses={200: UserSerializer(many=True)},
    summary="Tizimdan chiqish uchun endpoint",
    description="Tizimdan chiqish uchun endpoint.",
    tags=["Avtorizatsiyaga oid endpointlar"],
)
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            data = {
                'message': str(e),
            }
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)

@extend_schema(
    responses={200: UserProfileSerializer(many=True)},
    summary="Profile ma'lumotlari uchun endpoint",
    description="Profile ma'lumotlari uchun endpoint.",
    tags=["Profilega oid endpoint"],
)
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        data = {
            'success':True,
            'data': serializer.data,
        }
        return Response(data)
