import logging

logging.basicConfig(
    format="%(levelname)s — %(message)s"
)

logging.debug("Debug: using for deep code tracing")
logging.info("Info: process started successfully")
logging.warning("Warning: disk space is low")
logging.error("Error: failed to save file")
logging.critical("Critical: system crash detected")

logging.getLogger().setLevel(logging.DEBUG)
print("\n--- After setting level to DEBUG ---\n")

logging.debug("Debug: now visible after level change")