import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
console_handler.setFormatter(console_formatter)

file_handler = logging.FileHandler("service.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("DEBUG: connecting to database")
logger.info("INFO: connection established")
logger.warning("WARNING: query took too long")
logger.error("ERROR: failed to fetch data")
logger.critical("CRITICAL: system crash")
logger.info("INFO: Program finished successfully")

