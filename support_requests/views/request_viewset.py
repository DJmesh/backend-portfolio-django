from rest_framework import viewsets
from support_requests.models import SupportRequest
from support_requests.serializers import SupportRequestSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    list=extend_schema(
        tags=['Suporte'],
        description="Lista e cria solicitações de suporte. Por padrão, o sistema armazena no máximo 20 registros.\n"
                    "Se o limite for atingido, a solicitação mais antiga será apagada automaticamente."
    ),
    retrieve=extend_schema(tags=['Suporte']),
    create=extend_schema(tags=['Suporte']),
    update=extend_schema(tags=['Suporte']),
    partial_update=extend_schema(tags=['Suporte']),
    destroy=extend_schema(tags=['Suporte']),
)
class SupportRequestViewSet(viewsets.ModelViewSet):
    queryset = SupportRequest.objects.all().order_by("-created_at")
    serializer_class = SupportRequestSerializer

    def perform_create(self, serializer):
        max_supports = 20
        if SupportRequest.objects.count() >= max_supports:
            oldest_request = SupportRequest.objects.order_by('created_at').first()
            oldest_request.delete()
        serializer.save()
