from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'

    def ready(self):
        print("Starting Scheduler ...")
        from .scheduler import updater
        updater.start()
