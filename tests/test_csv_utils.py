import tempfile
import unittest
from pathlib import Path

from tp_utils.csv_utils import write_csv_file, read_csv_file


class CSVUtilsTestCase(unittest.TestCase):
    def test_csv_roundtrip(self):
        table0 = []
        table1 = [
            ["fred"],
            ["dave", "bill"],
        ]
        for table in [table0, table1]:
            with tempfile.TemporaryDirectory() as tmpdir:
                path = Path(tmpdir) / "test.csv"
                write_csv_file(path, table)
                table2 = read_csv_file(path)
                self.assertEqual(table2, table)
