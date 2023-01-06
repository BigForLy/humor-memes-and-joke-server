import os


LOG_LEVEL = os.getenv("HUMOR_LOG_LEVEL", "INFO")
LOG_FILE_PATH = "humor-log.log"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
        },
        "file": {
            "format": "%(asctime)s.%(msecs)03d %(levelname)-6s %(name)s - %(message)s",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "formatter": "file",
            "class": "logging.FileHandler",
            "filename": LOG_FILE_PATH,
        },
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["default", "file"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "uvicorn.error": {"level": LOG_LEVEL},
        "uvicorn.access": {
            "handlers": ["access", "file"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["default", "file"],
        "level": LOG_LEVEL,
        "propagate": False,
    },
}
