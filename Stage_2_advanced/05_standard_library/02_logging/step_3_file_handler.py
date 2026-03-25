import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log", mode="w")

formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("Debug: checking file logging")
logger.info("Info: writing to log file started")
logger.warning("Warning: disk space low")
logger.error("Error: failed to open file")
logger.critical("Critical: program crashed")
