from contextlib import contextmanager

@contextmanager
def open_log(file_path):
    log_file = open(file_path, "a", encoding="utf-8")
    try:
        log_file.write("=== Log session started ===\n")
        yield log_file
    finally:
        log_file.write("=== Log session ended ===\n\n")
        log_file.close()