"""
Settings for local development.

These settings are not fast or efficient, but allow local servers to be run
using the django-admin.py utility.

This file should be excluded from version control to keep the settings local.
"""

import os
import os.path

from .base import *  # pylint: disable=unused-wildcard-import,wildcard-import

# Run in debug mode.

DEBUG = True

TEMPLATE_DEBUG = DEBUG


# Save media files to the user's Sites folder.

MEDIA_ROOT = os.path.expanduser(os.path.join("~/Sites", SITE_DOMAIN, "media"))
STATIC_ROOT = os.path.expanduser(os.path.join("~/Sites", SITE_DOMAIN, "static"))
NODE_MODULES_ROOT = os.path.expanduser(os.path.join("~/Workspace/dangamble", "node_modules"))


# Use local server.

SITE_DOMAIN = "localhost:8000"

PREPEND_WWW = False


# Disable the template cache for development.

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)


# Optional separate database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": "localhost",
        "NAME": "dangamble",
        "USER": os.getlogin(),
    },
}

# Mailtrip SMTP
EMAIL_HOST = 'mailtrap.io'
EMAIL_HOST_USER = '178288370161874a6'
EMAIL_HOST_PASSWORD = '5033a6d5bca3f0'
EMAIL_PORT = '2525'
EMAIL_USE_TLS = True


def frontend_templates():
    return [
        str(f[:-5])
        for f in os.listdir(os.path.join(TEMPLATE_DIRS[0], 'frontend'))
        if f[:1] != '_'
    ]
