from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from activity_log.models import UserActivity
from activity_log.serializers import UserActivitySerializer
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    list=extend_schema(
        tags=['Atividades'],
        description="Essa view só pode ser acessada com autenticação JWT.\n\n"
                    " Faça um `POST` para `/auth/token/` com `email` e `password` para obter um token.\n"
                    " Use o token no cabeçalho como: `Authorization:<token>`."
    ),
    retrieve=extend_schema(tags=['Atividades']),
    create=extend_schema(tags=['Atividades']),
    update=extend_schema(tags=['Atividades']),
    partial_update=extend_schema(tags=['Atividades']),
    destroy=extend_schema(tags=['Atividades']),
)
class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all().order_by('-timestamp')
    serializer_class = UserActivitySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        max_logs = 20
        if UserActivity.objects.count() >= max_logs:
            oldest_log = UserActivity.objects.order_by('timestamp').first()
            oldest_log.delete()
        serializer.save()
