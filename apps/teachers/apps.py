from django.apps import AppConfig

class TeachersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.teachers'  # ✅ deve incluir o prefixo 'apps.'
