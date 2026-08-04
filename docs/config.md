# Configuration

Store project-wide settings in one place.

**Includes**
-   Project paths (PROJECT_ROOT, SOURCE_DIR, LOG_DIR)
-   Default Git settings (DEFAULT_BRANCH)
-   Log settings (LOG_FILE, LOG_LEVEL)
-   Other values shared by multiple modules

**Use**
-   Change settings in one place.
-   Avoid hardcoding values across files.
-   Keep the project organized.

**pathlib.path**
-   Cross-platform (Windows/Linux/macOS)
-   Easy path joining: PROJECT_ROOT / "demo_html"