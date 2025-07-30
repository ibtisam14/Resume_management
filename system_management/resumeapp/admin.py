from django.contrib import admin
from django.utils.html import format_html
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):

    list_display = ('id', 'user_email', 'status', 'submitted_at', 'resume_file')
    list_filter = ('status', 'submitted_at')

    search_fields = ('user__email',)


    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'

    def resume_file(self, obj):
        if obj.file:
            return format_html("<a href='{}' target='_blank'>View PDF</a>", obj.file.url)
        return "No file uploaded"
    resume_file.short_description = "Resume File"
