from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from django.contrib.auth import authenticate,get_user_model
from .serializers import UsuarioSerializer


class RegistroView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        print(f"Email recibido: {email}")  # Verifica si llega el email
        print(f"Password recibido: {password}")

        try:
            user = Usuario.objects.get(email=email)
            print("Usuario encontrado:", user.email)
            if user.check_password(password):
                return Response({"message": "Login exitoso"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        except Usuario.DoesNotExist:
            return Response({"message": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
