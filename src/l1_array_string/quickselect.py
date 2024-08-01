from typing import List


def quickselect(arr: List[int], k: int) -> int:
    return qs(arr, k - 1, 0, len(arr) - 1)


def qs(arr: List[int], k: int, start: int, end: int) -> int:
    if start >= end:
        return arr[k]

    middle = (start + end) // 2
    pivot = arr[middle]

    # partition
    left, right = start, end

    while left <= right:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    if k <= right:
        return qs(arr, k, start, right)
    if k >= left:
        return qs(arr, k, left, end)

    return arr[k]
