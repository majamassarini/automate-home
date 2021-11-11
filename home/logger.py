# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging  # noqa
import os


def default_logging_configuration(
    logging_dir,
    logging_level="INFO",
    knx_logging_level="INFO",
    lifx_logging_level="INFO",
    sonos_logging_level="INFO",
    somfy_sdn_logging_level="INFO",
    home_assistant_logging_level="INFO",
):
    return {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s:%(lineno)d %(levelname)s - %(message)s",
            },
            "collector": {
                "format": "%(asctime)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "formatter": "simple",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "home": {
                "formatter": "simple",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(logging_dir, "home.log"),
                "when": "midnight",
                "interval": 1,
            },
            "knx": {
                "formatter": "simple",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(logging_dir, "knx.log"),
                "when": "midnight",
                "interval": 1,
            },
            "lifx": {
                "formatter": "simple",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(logging_dir, "lifx.log"),
                "when": "midnight",
                "interval": 1,
            },
            "sonos": {
                "formatter": "simple",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(logging_dir, "sonos.log"),
                "when": "midnight",
                "interval": 1,
            },
            "somfy_sdn": {
                "formatter": "simple",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(logging_dir, "somfy-sdn.log"),
                "when": "midnight",
                "interval": 1,
            },
            "home_assistant": {
                "formatter": "simple",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(logging_dir, "home_assistant.log"),
                "when": "midnight",
                "interval": 1,
            },
        },
        "loggers": {
            "": {
                "level": "INFO",
                "handlers": ["console", "home"],
                "propagate": True,
            },
            "asyncio": {
                "level": "WARNING",
                "handlers": ["console", "home"],
                "propagate": False,
            },
            "apscheduler": {
                "level": "WARNING",
                "handlers": ["console", "home"],
                "propagate": False,
            },
            "home": {
                "level": logging_level,
                "handlers": ["console", "home"],
                "propagate": False,
            },
            "knx_stack": {
                "level": knx_logging_level,
                "handlers": ["console", "knx"],
                "propagate": False,
            },
            "knx_plugin": {
                "level": knx_logging_level,
                "handlers": ["console", "knx"],
                "propagate": False,
            },
            "lifx": {
                "level": lifx_logging_level,
                "handlers": ["console", "lifx"],
                "propagate": False,
            },
            "lifx_plugin": {
                "level": lifx_logging_level,
                "handlers": ["console", "lifx"],
                "propagate": False,
            },
            "soco": {
                "level": sonos_logging_level,
                "handlers": ["console", "sonos"],
                "propagate": False,
            },
            "soco_plugin": {
                "level": sonos_logging_level,
                "handlers": ["console", "sonos"],
                "propagate": False,
            },
            "somfy_sdn": {
                "level": somfy_sdn_logging_level,
                "handlers": ["console", "somfy_sdn"],
                "propagate": False,
            },
            "somfy_sdn_plugin": {
                "level": somfy_sdn_logging_level,
                "handlers": ["console", "somfy_sdn"],
                "propagate": False,
            },
            "home_assistant_plugin": {
                "level": home_assistant_logging_level,
                "handlers": ["console", "home_assistant"],
                "propagate": False,
            },
        },
    }
