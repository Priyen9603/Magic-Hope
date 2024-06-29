from django.apps import AppConfig


class WellnessConfig(AppConfig):
    name = 'wellness'
# wellness/apps.py





class WellnessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wellness'

    def ready(self):
        import wellness.signals  # Import the signals module

