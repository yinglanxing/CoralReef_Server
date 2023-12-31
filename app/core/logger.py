import json
import logging.config
import os

from config import settings

path = settings.LOGGING_CONFIG_FILE
if os.path.exists(path):
    with open(path, "r") as f:
        config = json.load(f)
        logging.config.dictConfig(config)
else:
    logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("log")
