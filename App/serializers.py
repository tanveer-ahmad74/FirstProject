from rest_framework import serializers
from App.models import Colors
from django.contrib.auth import get_user_model

User = get_user_model()


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ['id', 'color_name', 'hex_color_code']


class UserSerializer(serializers.ModelSerializer):
    color_name = serializers.CharField(source='color.color_name', read_only=True)
    full_name = serializers.CharField(read_only=True)
    is_delete = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        exclude = ['date_joined', 'groups', 'user_permissions', 'is_active', 'is_staff',
                   'last_login', 'is_superuser']

