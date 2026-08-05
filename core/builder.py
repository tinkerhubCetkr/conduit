from core.config import SOURCE_DIR
from core.logger import logger

HTML_EXTENSIONS = {".html", ".htm"}
CSS_EXTENSIONS = {".css"}
JS_EXTENSIONS = {".js"}

IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
}


def discover_assets():
    """
    Scan the source directory and categorize project assets.

    Returns:
        dict: Dictionary containing categorized asset paths.
    """

    logger.info("Starting asset discovery")

    # Check if the source directory exists
    if not SOURCE_DIR.exists():
        logger.error(f"Source directory '{SOURCE_DIR}' not found.")
        return None

    assets = {
        "html": [],
        "css": [],
        "javascript": [],
        "images": [],
        "other": []
    }

    # Scan all files recursively
    for file in SOURCE_DIR.rglob("*"):

        if not file.is_file():
            continue

        suffix = file.suffix.lower()

        if suffix in HTML_EXTENSIONS:
            assets["html"].append(file)

        elif suffix in CSS_EXTENSIONS:
            assets["css"].append(file)

        elif suffix in JS_EXTENSIONS:
            assets["javascript"].append(file)

        elif suffix in IMAGE_EXTENSIONS:
            assets["images"].append(file)

        else:
            assets["other"].append(file)

    logger.info(
        f"Asset discovery completed | "
        f"HTML: {len(assets['html'])}, "
        f"CSS: {len(assets['css'])}, "
        f"JavaScript: {len(assets['javascript'])}, "
        f"Images: {len(assets['images'])}, "
        f"Other: {len(assets['other'])}"
    )

    return assets