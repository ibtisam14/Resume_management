from django.db import models
from django.conf import settings

class Resume(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume by {self.user.email} - {self.status}"
