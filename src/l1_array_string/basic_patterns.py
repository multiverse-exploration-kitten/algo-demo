from collections import defaultdict
from typing import List


def two_sum_sorted_arr(arr: List[int], target: int) -> List[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


def move_zeros(arr: List[int]) -> List[int]:
    insert_pos = 0
    for num in arr:
        if num != 0:
            arr[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(arr):
        arr[insert_pos] = 0
        insert_pos += 1
    return arr


def max_sum_subarray(arr: List[int], k: int) -> int:
    n = len(arr)
    max_sum = sum(arr[:k])
    current_sum = max_sum
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum


def min_subarray_len(arr: List[int], target: int) -> int:
    n = len(arr)
    left = 0
    current_sum = 0
    min_length = float("inf")
    for right in range(n):
        current_sum += arr[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    return min_length if min_length != float("inf") else 0


def prefix_sum(arr):
    n = len(arr)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + arr[i]
    return prefix_sums


def subarray_sum(prefix_sums, i, j):
    return prefix_sums[j + 1] - prefix_sums[i]


def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


def count_subarray_sum_for_target(nums, target):
    count = 0
    current_sum = 0
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    for num in nums:
        current_sum += num
        count += prefix_sums[current_sum - target]
        prefix_sums[current_sum] += 1
    return count
