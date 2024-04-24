from users.serializers import UserSerializer,UserProfileSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
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
class UserLoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)
            return Response({'token': token.key, 'username': user.username, 'role': user.role})
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


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
        print(request.headers)
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()

        return Response({'detail': 'Successfully logged out.'})


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
