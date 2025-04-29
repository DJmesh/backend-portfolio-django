from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    list=extend_schema(tags=['Usuários']),
    retrieve=extend_schema(tags=['Usuários']),
    create=extend_schema(tags=['Usuários']),
    update=extend_schema(tags=['Usuários']),
    partial_update=extend_schema(tags=['Usuários']),
    destroy=extend_schema(tags=['Usuários']),
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('created_at')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        max_users = 5
        if User.objects.count() >= max_users:
            oldest_user = User.objects.order_by('created_at').first()
            oldest_user.delete()
        serializer.save()
