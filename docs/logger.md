# Logger   

Provide one centralized logger for the whole project.

*imported builtin python logging module*

**Why use a wrapper?**
-   Configure logging in one place.
-   Keep all modules consistent.
-   Easier to modify later.

**Responsibilities**
-   Create the logs directory.
-   Configure the logging system.
-   Export a shared logger object.

**Workflow**
Project modules → core/logger.py → Python logging module → logs/automation.log

**Usage**
*from core.logger import logger*

*logger.info(“Repository cloned”)* 
*logger.warning(“Missing file”)*
*logger.error(“Push failed”)*