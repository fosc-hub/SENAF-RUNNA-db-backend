# api/serializers.py
'''
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
'''

from rest_framework import serializers
from infrastructure.models import (
    TProvincia, TDepartamento, TLocalidad, TBarrio, TCPC, TLocalizacion
)

from infrastructure.models import CustomUser
from django.contrib.auth.models import Group, Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']

class GroupSerializer(serializers.ModelSerializer):
    # permissions = PermissionSerializer(many=True, source='permissions.all')

    class Meta:
        model = Group
        fields = ['id', 'name'] #'permissions']


class CustomUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)  # Serialize groups with permissions
    # user_permissions = PermissionSerializer(many=True)
    all_permissions = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'fecha_nacimiento', 'genero', 'telefono', 'is_staff',
            'is_active', 'is_superuser', 'groups', 'user_permissions',
            'all_permissions'
        ]

    def get_all_permissions(self, obj):
        """Return both user-specific and group-inherited permissions."""
        # Collect both direct and group permissions
        permissions = obj.user_permissions.all() | Permission.objects.filter(group__user=obj)
        return PermissionSerializer(permissions, many=True).data


class TProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TProvincia
        fields = '__all__'

class TDepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDepartamento
        fields = '__all__'

class TLocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalidad
        fields = '__all__'

class TBarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBarrio
        fields = '__all__'

class TCPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCPC
        fields = '__all__'

class TLocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacion
        fields = '__all__'
