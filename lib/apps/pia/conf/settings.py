#
#  Configuration Files
#
LOGIN_CONFIG = '/home/iainstott/GitRepo/Scripts/lib/gui/pia/login.conf'
PIA_CONFIG = '/home/iainstott/GitRepo/Scripts/lib/gui/pia/pia.conf'
PIA_HOST_LIST = '/home/iainstott/GitRepo/Scripts/lib/gui/pia/vpn-hosts.txt'

#
# Debugging information
#
DEBUG = False


#
# Logging configuration for Python's logging module
#
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "pia.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "pia.utils.log.RequireDebugTrue"
        }
    },
    "handlers": {
        "null": {
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
    },
    "loggers": {
        "pia": {
            "level": "INFO",
            "handlers": ["console"],
        },
    },
}
