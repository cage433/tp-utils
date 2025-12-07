from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
from time import sleep
from unittest import TestCase

from tp_random_tests.random_test_case import RandomisedTest

from tp_utils.shelf_lock import locked_shelf


def _cached_calculation(shelf_path: Path, n: int):
    sleep(0.01)
    with locked_shelf(shelf_path) as shelve:
        key = str(n)
        if key not in shelve:
            shelve[key] = n * n

        return shelve[key]


class ShelfLockTestCase(TestCase):

    @RandomisedTest()
    def test_shelf_works(self, rng):
        with TemporaryDirectory() as tmp_dir:
            shelf_path = Path(tmp_dir) / "test_shelf"
            futures = []
            with ProcessPoolExecutor(max_workers=4) as executor:
                for _ in range(20):
                    n_squared = executor.submit(_cached_calculation, shelf_path, rng.randint(100))
                    futures.append(n_squared)
            for f in futures:
                self.assertTrue(f.result() >= 0)
