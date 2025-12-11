import unittest

from tp_utils.list_utils import ListUtils


class ListUtilsTestCase(unittest.TestCase):
    def test_empty_group_into(self):
        grouped = ListUtils.group_into([], lambda v: v % 2)
        self.assertEqual(0, len(grouped))

    def test_group_into(self):
        values = [1, 2, 3, 4, 4]
        grouped = ListUtils.group_into(values, lambda v: v % 2)

        self.assertEqual([1, 3], grouped[1])
        self.assertEqual([2, 4, 4], grouped[0])

    def test_partition(self):
        values = []
        true_values, false_values = ListUtils.partition(values, lambda v: v % 2 == 0)
        self.assertEqual(0, len(true_values))
        self.assertEqual(0, len(false_values))

        values = [1, 2, 11, 1]
        true_values, false_values = ListUtils.partition(values, lambda v: v % 2 == 0)
        self.assertEqual([2], true_values)
        self.assertEqual([1, 11, 1], false_values)
