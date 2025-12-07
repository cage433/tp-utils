import shelve
from contextlib import contextmanager
from pathlib import Path

from fcntl import flock, LOCK_UN, LOCK_EX


# from
# https://stackoverflow.com/questions/486490/python-shelve-module-question
@contextmanager
def locked_shelf(shelf_path: Path):
    with open(shelf_path.with_suffix(".lock"), 'w') as lock:
        flock(lock.fileno(), LOCK_EX)  # block until lock is acquired
        try:
            with shelve.open(str(shelf_path)) as shelf:
                yield shelf
        finally:
            flock(lock.fileno(), LOCK_UN)  # release



