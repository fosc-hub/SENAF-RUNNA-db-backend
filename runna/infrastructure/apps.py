from django.apps import AppConfig

class InfrastructureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'infrastructure'

    def ready(self):
        print("InfrastructureConfig is ready!")  # Add this line

        import infrastructure.signals