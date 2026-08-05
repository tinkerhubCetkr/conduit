# builder

Prepares project assets for publishing.

**Responsibilities**
- Read files from the source directory.
- Discover HTML, CSS, JS, and image assets.
- Organize assets for the publishing pipeline.
- Return structured information for other modules.

**Workflow**
SOURCE_DIR -> Check exists -> Scan recursively (rglob(“*“)) -> Skip
folders (is_file()) -> Get extension (suffix.lower()) -> Categorize ->
Log summary -> Return dictionary


