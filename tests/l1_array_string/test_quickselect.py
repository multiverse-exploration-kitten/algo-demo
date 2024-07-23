import random
import unittest

from src.l1_array_string.quickselect import quickselect


class TestQuickselect(unittest.TestCase):
    def test_quickselect(self):
        k = random.randint(0, 10)
        random_arr = [random.randint(0, 100) for _ in range(10)]

        sorted_arr = sorted(random_arr)
        self.assertEqual(quickselect(random_arr, k), sorted_arr[k - 1])


if __name__ == "__main__":
    unittest.main()
