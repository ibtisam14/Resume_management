from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_email', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('user__email',)

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'
