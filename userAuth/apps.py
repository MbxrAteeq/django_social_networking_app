from django.apps import AppConfig
from django.core.signals import request_finished


class UserauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userAuth'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals
        # Explicitly connect a signal handler.
        request_finished.connect(signals.enrich_user_data)
