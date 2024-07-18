import random


def my_sort(arr):
    qs(arr, 0, len(arr) - 1)
    return arr


def qs(arr, start, end):
    if start >= end:
        return

    middle = (start + end) // 2
    pivot = arr[middle]

    # partition
    left, right = start, end

    while left <= right:
        while left <= right and pivot > arr[left]:
            left += 1
        while left <= right and pivot < arr[right]:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    qs(arr, start, right)
    qs(arr, left, end)


if __name__ == "__main__":
    random_arr = [random.randint(0, 100) for _ in range(10)]

    sorted_arr = sorted(random_arr)
    my_sort(random_arr)
    assert sorted_arr == random_arr
