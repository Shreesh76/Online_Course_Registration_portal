from django.apps import AppConfig


class ValidateConfig(AppConfig):
    name = 'validate'

    def ready(self):
        import validate.signals

