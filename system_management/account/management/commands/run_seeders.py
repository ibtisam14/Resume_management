from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed database with admin user only'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(email='admin@gmail.com').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@gmail.com',
                password='admin123',
                is_admin=True
            )
            self.stdout.write(self.style.SUCCESS('✅ Created admin user with email: admin@gmail.com'))
        else:
            self.stdout.write(self.style.NOTICE('ℹ️ "SKIPPING": Admin user with email admin@gmail.com already exists'))
