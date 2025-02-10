import logging.config
import os

import celery

from yumgo_python_template.config.logs import LOGGING

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "yumgo_python_template.config.settings.local",
)

celery_app = celery.Celery(
    __name__,
)

celery_app.config_from_object("yumgo_python_template.celeryconfig")

logging.config.dictConfig(LOGGING)
