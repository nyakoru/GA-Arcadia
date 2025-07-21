import logging
from command.tools.ArcaneUtils import misc
from pathlib import Path

# Create the Logs directory if it doesn't exist
log_path = Path(__file__).parent.parent.parent/"logs"
misc.mkdir(log_path)

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Handlers
info_handler = logging.FileHandler(f'{log_path}/info.log', encoding='utf-8')
info_handler.setLevel(logging.INFO)

error_handler = logging.FileHandler(f'{log_path}/error.log', encoding='utf-8')
error_handler.setLevel(logging.ERROR)

warning_handler = logging.FileHandler(f'{log_path}/warning.log', encoding='utf-8')
warning_handler.setLevel(logging.WARNING)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
warning_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(warning_handler)
logger.addHandler(console_handler)