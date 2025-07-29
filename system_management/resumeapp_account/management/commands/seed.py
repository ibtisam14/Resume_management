from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed database with only the admin user'

    def handle(self, *args, **kwargs):
        # Delete test user if exists
        if User.objects.filter(email='ibtisam@gmail.com').exists():
            User.objects.filter(email='ibtisam@gmail.com').delete()
            self.stdout.write(self.style.WARNING('⚠️ Deleted test user: ibtisam@gmail.com'))

        # Create admin user if not exists
        if not User.objects.filter(email='admin@example.com').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✅ Created admin user'))
