import logging
from core.config import LOG_DIR, LOG_FILE, LOG_LEVEL

# Create the logs directory if it doesn't exist
LOG_DIR.mkdir(exist_ok=True)

# Full path to the log file
log_path = LOG_DIR / LOG_FILE

# Configure the logging system
logging.basicConfig(
    filename=log_path,
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Create a logger object for the project
logger = logging.getLogger("conduit")