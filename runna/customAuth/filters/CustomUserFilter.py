from django_filters import rest_framework as filters
from customAuth.models import CustomUser
from django.contrib.auth.models import Group

class CustomUserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='icontains')  # Partial match for username
    email = filters.CharFilter(lookup_expr='icontains')  # Partial match for email
    is_staff = filters.BooleanFilter()  # Filter by staff status
    is_active = filters.BooleanFilter()  # Filter by active status
    is_superuser = filters.BooleanFilter()
    groups = filters.ModelMultipleChoiceFilter(queryset=Group.objects.all())  # Filter by group
    localidad = filters.ModelMultipleChoiceFilter(queryset=Group.objects.all())

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_staff', 'is_active', 'groups', 'localidad', 'equipo']
        