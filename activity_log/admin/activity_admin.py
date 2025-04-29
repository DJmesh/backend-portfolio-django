from django.contrib import admin
from activity_log.models import UserActivity

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "timestamp")
    list_filter = ("action", "timestamp")
    search_fields = ("user__username", "details")
