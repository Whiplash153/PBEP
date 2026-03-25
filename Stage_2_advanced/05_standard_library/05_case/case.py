import os
import logging
from datetime import datetime, timedelta
from pathlib import Path

base_dir = Path.cwd()
logs_dir = base_dir / "logs"
logs_dir.mkdir(exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
log_file = logs_dir / f"{today}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

logging.info("Program started.")
logging.info(f"Log file created: {log_file.name}")
logging.info(f"User: {os.environ.get('USER', 'unknown')}")

for file in logs_dir.glob("*.log"):
    timestamp = datetime.strptime(file.stem, "%Y-%m-%d")
    if datetime.now() - timestamp > timedelta(days=3):
        file.unlink()
        logging.info(f"Old log removed: {file.name}")

files_count = len(list(logs_dir.glob("*.log")))

print("Current log file:", log_file)
print("Logs in folder:", files_count)
print("=== DONE ===")