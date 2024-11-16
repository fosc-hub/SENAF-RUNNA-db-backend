from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from infrastructure.models import CustomUser

class Command(BaseCommand):
    help = 'Sets up the project by making migrations, migrating, and creating a superuser'

    def handle(self, *args, **kwargs):
        try:
            # Step 1: Make migrations
            self.stdout.write('Making migrations...')
            call_command('makemigrations')
            self.stdout.write(self.style.SUCCESS('Migrations created successfully.'))

            # Step 2: Apply migrations
            self.stdout.write('Applying migrations...')
            call_command('migrate')
            self.stdout.write(self.style.SUCCESS('Migrations applied successfully.'))

            # Step 3: Create superuser
            if not CustomUser.objects.filter(username='admin').exists():
                self.stdout.write('Creating superuser...')
                CustomUser.objects.create_superuser(
                    username='admin',
                    email='admin@gmail.com',
                    password='pepe1234'
                )
                self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
            else:
                self.stdout.write(self.style.WARNING('Superuser already exists.'))

        except CommandError as e:
            raise CommandError(f"Error: {e}")
