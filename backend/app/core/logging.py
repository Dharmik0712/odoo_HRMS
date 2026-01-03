import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
        }
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["default"],
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("dayflow")
