from pathlib import Path
import logging

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Directories
SOURCE_DIR = PROJECT_ROOT / "demo_html"
LOG_DIR = PROJECT_ROOT / "logs"

# Git
DEFAULT_BRANCH = "main"

# Logging
LOG_FILE = "automation.log"
LOG_LEVEL = logging.INFO