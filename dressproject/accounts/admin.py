from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'nickname', 'gender', 'difficulty', 'is_staff', 'date_joined')
    search_fields = ('nickname', 'gender')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('user_id',)
        return ()
