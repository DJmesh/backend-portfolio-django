from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from users.views.me_view import MeView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
    path('', include(router.urls)),
]
