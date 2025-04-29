from rest_framework import serializers
from activity_log.models import UserActivity

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = "__all__"
