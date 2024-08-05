from django.apps import AppConfig
## this import is uset to make our django app coverted to any languages and its a good practice
from django.utils.translation import gettext_lazy as _

class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.profiles"
    verbose_name = _("Profiles")