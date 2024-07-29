from typing import Callable, List


def binary_search_exact(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def binary_search_first_occurrence(arr: List[int], target: int) -> int:
    # left bound
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    if left < len(arr) and arr[left] == target:
        return left
    return -1


def binary_search_last_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    if arr[left - 1] != target:
        return -1
    return left - 1


def find_peak(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid
        else:
            right = mid

    if arr[left] >= arr[right]:
        return left
    return right


def ternary_search_max(
    f: Callable[[float], float], left: float, right: float, absolute_precision: float
) -> float:
    while right - left > absolute_precision:
        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3
        if f(left_third) < f(right_third):
            left = left_third
        else:
            right = right_third
    return (left + right) / 2


def can_place(arr: List[int], n: int, k: int, mid: int) -> bool:
    count = 1
    last_position = arr[0]
    for i in range(1, n):
        if arr[i] - last_position >= mid:
            count += 1
            last_position = arr[i]
        if count >= k:
            return True
    return False


def find_largest_min_distance(arr: List[int], k: int) -> int:
    arr.sort()
    n = len(arr)
    left, right = 0, arr[-1] - arr[0]
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if can_place(arr, n, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


def search_2d_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
