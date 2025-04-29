from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema_view, extend_schema
from config.views import CustomLoginView

@extend_schema_view(
    post=extend_schema(tags=['Autenticação']),
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass

@extend_schema_view(
    post=extend_schema(tags=['Autenticação']),
)
class CustomTokenRefreshView(TokenRefreshView):
    pass

urlpatterns = [
    path('admin/login/', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),

    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include('users.urls')),
    path('api/', include('support_requests.urls')),
    path('api/', include('activity_log.urls')),
]
