import logging, os
import logging.handlers
from app import config

logger = logging.getLogger("Istaroth")
logger.setLevel(logging.INFO)
_log_file = os.path.join(config.LOGS,"istaroth.log")
_handler = logging.handlers.TimedRotatingFileHandler(_log_file, when='midnight', interval=1, backupCount=6)
_handler.setLevel(logging.INFO)
_formatter = logging.Formatter('\n%(asctime)s - [%(name)s] - %(levelname)s - %(message)s\n')
_handler.setFormatter(_formatter)
logger.addHandler(_handler)
_werkzeug_logger = logging.getLogger('werkzeug')
_werkzeug_logger.setLevel(logging.CRITICAL)
