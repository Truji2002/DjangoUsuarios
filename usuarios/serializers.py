from rest_framework import serializers
from .models import Usuario


from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'nombre', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Extraemos la contraseña
        instance = Usuario.objects.create_user(password=password, **validated_data)
        return instance
