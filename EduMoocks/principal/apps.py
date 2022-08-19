from django.apps import AppConfig


class PrincipalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'principal'
    verbose_name= "Bases de datos"
    
    def ready(self):
        import principal.signals
