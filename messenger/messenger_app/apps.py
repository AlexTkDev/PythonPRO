from django.apps import AppConfig


class MessengerAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "messenger_app"
    verbose_name = "Все записи пользователей"

    def ready(self):
        import messenger_app.signals