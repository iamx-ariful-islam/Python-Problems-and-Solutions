# pip install rich

import logging
from rich.logging import RichHandler


logging.basicConfig(
    level="DEBUG", 
    handlers=[RichHandler(rich_tracebacks=True)]
)

logger = logging.getLogger("rich-logger")
logger.debug("Just a debug message, but pretty!")