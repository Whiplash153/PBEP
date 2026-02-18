import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
console_handler.setFormatter(console_formatter)

file_handler = logging.FileHandler("combined.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("DEBUG: testing combined handlers")
logger.info("INFO: console won't show this")
logger.warning("WARNING: console and file both show this")
logger.error("ERROR: something went wrong")
logger.critical("Critical: program crashed")