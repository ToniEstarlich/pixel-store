import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "clothing_store.settings"
)

django.setup()
