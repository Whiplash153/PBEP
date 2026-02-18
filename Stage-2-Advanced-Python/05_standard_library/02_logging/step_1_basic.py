import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debug: used for code debugging")
logging.info("Info: program is running normally")
logging.warning("Warning: potential issue")
logging.error("Error: an error occurred")
logging.critical("Critical: serious error, program may stop")
