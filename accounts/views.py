from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import CustomUser

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},status=HTTP_201_CREATED)
        return Response (serializer.errors,status=HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},status=HTTP_201_CREATED)
        return Response({"error":"Invalid credentials"},status=HTTP_400_BAD_REQUEST)

class ProfileApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"user":request.user.username})