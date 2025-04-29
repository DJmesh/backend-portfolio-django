from django.urls import path, include
from rest_framework.routers import DefaultRouter
from support_requests.views.request_viewset import SupportRequestViewSet

router = DefaultRouter()
router.register(r'support', SupportRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
