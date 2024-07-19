import unittest

from src.l1_array_string.basic_patterns import (
    count_subarray_sum_for_target,
    first_missing_positive,
    max_sum_subarray,
    min_subarray_len,
    move_zeros,
    partition_array,
    prefix_sum,
    reverse_array,
    rotate_array_k_times,
    subarray_sum,
    two_sum_sorted_arr,
)


class TestBasicPatterns(unittest.TestCase):
    def test_two_sum_sorted_arr(self):
        test_cases = [
            ([1, 2, 3, 4, 6], 6, [1, 3]),
            ([2, 5, 9, 11], 11, [0, 2]),
            ([1, 3, 5, 7], 12, [2, 3]),
            ([1, 2, 3, 4], 8, [-1, -1]),
        ]
        for arr, target, expected in test_cases:
            with self.subTest(arr=arr, target=target, expected=expected):
                self.assertEqual(two_sum_sorted_arr(arr, target), expected)

    def test_move_zeros(self):
        test_cases = [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0, 0, 1], [1, 0, 0]),
            ([1, 0, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0]),
        ]
        for arr, expected in test_cases:
            with self.subTest(arr=arr, expected=expected):
                self.assertEqual(move_zeros(arr), expected)

    def test_max_sum_subarray(self):
        test_cases = [
            ([2, 1, 5, 1, 3, 2], 3, 9),
            ([2, 3, 4, 1, 5], 2, 7),
            ([1, 1, 1, 1, 1], 2, 2),
        ]
        for arr, k, expected in test_cases:
            with self.subTest(arr=arr, k=k, expected=expected):
                self.assertEqual(max_sum_subarray(arr, k), expected)

    def test_min_subarray_len(self):
        test_cases = [
            ([2, 1, 5, 2, 8], 7, 1),
            ([3, 4, 1, 1, 6], 8, 3),
            ([1, 1, 1, 1], 4, 4),
            ([1, 2, 3, 4, 5], 11, 3),
        ]
        for arr, target, expected in test_cases:
            with self.subTest(arr=arr, target=target, expected=expected):
                self.assertEqual(min_subarray_len(arr, target), expected)

    def test_prefix_sum(self):
        test_cases = [([1, 2, 3], [0, 1, 3, 6]), ([2, 3, 4], [0, 2, 5, 9])]
        for arr, expected in test_cases:
            with self.subTest(arr=arr, expected=expected):
                self.assertEqual(prefix_sum(arr), expected)

    def test_subarray_sum(self):
        test_cases = [([0, 1, 3, 6], 1, 2, 5), ([0, 2, 5, 9], 0, 2, 9)]
        for prefix_sums, i, j, expected in test_cases:
            with self.subTest(prefix_sums=prefix_sums, i=i, j=j, expected=expected):
                self.assertEqual(subarray_sum(prefix_sums, i, j), expected)

    def test_first_missing_positive(self):
        test_cases = [([1, 2, 0], 3), ([3, 4, -1, 1], 2), ([7, 8, 9, 11, 12], 1)]
        for nums, expected in test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(first_missing_positive(nums), expected)

    def test_count_subarray_sum_for_target(self):
        test_cases = [([1, 1, 1], 2, 2), ([1, 2, 3], 3, 2), ([1, -1, 1], 1, 3)]
        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target, expected=expected):
                self.assertEqual(count_subarray_sum_for_target(nums, target), expected)

    def test_partition_array(self):
        test_cases = [
            ([5, 1, 4, 2, 3], 3),
            ([9, 12, 3, 5, 14, 10, 10], 10),
            ([3, 3, 3, 3, 3], 3),
            ([5, 2, 4, 7, 8, 1, 3], 5),
            ([1, 2, 3, 4, 5], 6),
            ([5, 4, 3, 2, 1], 0),
            ([1, 1, 1, 1, 1, 1], 1),
            ([1], 1),
            ([], 5),
        ]
        for arr, pivot in test_cases:
            with self.subTest(arr=arr, pivot=pivot):
                result = partition_array(arr.copy(), pivot)
                less_than_pivot = [x for x in result if x < pivot]
                greater_equal_pivot = [x for x in result if x >= pivot]

                # Check that all elements less than the pivot are on the left side
                self.assertTrue(
                    all(x < pivot for x in less_than_pivot),
                    "Elements less than pivot are not correctly partitioned",
                )

                # Check that all elements greater than or equal to the pivot are on the right side
                self.assertTrue(
                    all(x >= pivot for x in greater_equal_pivot),
                    "Elements greater than or equal to pivot are not correctly partitioned",
                )

                # Ensure the combined result matches the length of the original array
                self.assertEqual(
                    len(result),
                    len(arr),
                    "The result array does not have the same length as the input array",
                )

    def test_rotate_array_k_times(self):
        test_cases = [
            ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
            ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),
        ]
        for arr, k, expected in test_cases:
            with self.subTest(arr=arr, k=k, expected=expected):
                self.assertEqual(rotate_array_k_times(arr, k), expected)

    def test_reverse_array(self):
        test_cases = [
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
            ([1, 2, 3], [3, 2, 1]),
            ([], []),
        ]
        for arr, expected in test_cases:
            with self.subTest(arr=arr, expected=expected):
                self.assertEqual(reverse_array(arr), expected)


if __name__ == "__main__":
    unittest.main()
