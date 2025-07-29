from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed database with demo users'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(email='admin@example.com').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✅ Created admin user'))

        if not User.objects.filter(email='ibtisam@gmail.com').exists():
            User.objects.create_user(
                username='ibtisam',
                email='ibtisam@gmail.com',
                password='12345-ibt'
            )
            self.stdout.write(self.style.SUCCESS('✅ Created test user: ibtisam'))

        # Add more fake users here if needed
