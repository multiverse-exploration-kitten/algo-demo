def permute(nums, start, result):
    if start == len(nums):
        result.append(nums[:])
        return
    for i in range(start, len(nums)):
        swap(nums, start, i)
        permute(nums, start + 1, result)
        swap(nums, start, i)


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


# get next permutation
def next_permutation(nums):
    if len(nums) <= 1:
        return

    # Find the first index from the end where the number is smaller than the next number
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Find the first number from the end that is larger than nums[i]
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1

        swap(nums, i, j)

    # Reverse the sequence from i+1 to the end of the list
    reverse(nums, i + 1, len(nums) - 1)


def reverse(nums, start, end):
    while start < end:
        swap(nums, start, end)
        start += 1
        end -= 1


# Generate all combinations of a list.
def combinations(nums, k):
    result = []
    combinations_helper(nums, k, 0, [], result)
    return result


def combinations_helper(nums, k, start, path, result):
    if len(path) == k:
        result.append(path[:])
        return
    for i in range(start, len(nums)):
        path.append(nums[i])
        combinations_helper(nums, k, i + 1, path, result)
        path.pop()


# Find all unique combinations of numbers that sum up to a target.
def combination_sum(candidates, target):
    result = []
    combination_sum_helper(candidates, target, 0, [], result)
    return result


def combination_sum_helper(candidates, target, start, path, result):
    if target == 0:
        result.append(path[:])
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        path.append(candidates[i])
        combination_sum_helper(candidates, target - candidates[i], i, path, result)
        path.pop()


# Generate all subsets of a list.
def subsets(nums):
    result = []
    subsets_helper(nums, 0, [], result)
    return result


def subsets_helper(nums, start, path, result):
    result.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        subsets_helper(nums, i + 1, path, result)
        path.pop()


# Find all unique combinations of numbers that sum up to a target, where each number can be used only once.
def combination_sum2(candidates, target):
    candidates.sort()
    result = []
    combination_sum2_helper(candidates, target, 0, [], result)
    return result


def combination_sum2_helper(candidates, target, start, path, result):
    if target == 0:
        result.append(path[:])
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        path.append(candidates[i])
        combination_sum2_helper(candidates, target - candidates[i], i + 1, path, result)
        path.pop()


# Generate all possible letter combinations that the number could represent.
def letter_combinations(digits):
    if not digits:
        return []

    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []
    letter_combinations_helper(digits, 0, [], result, phone_map)
    return result


def letter_combinations_helper(digits, index, path, result, phone_map):
    if index == len(digits):
        result.append("".join(path))
        return
    letters = phone_map[digits[index]]
    for letter in letters:
        path.append(letter)
        letter_combinations_helper(digits, index + 1, path, result, phone_map)
        path.pop()


# Partition a string such that every substring is a palindrome.
def partition(s):
    result = []
    partition_helper(s, 0, [], result)
    return result


def partition_helper(s, start, path, result):
    if start == len(s):
        result.append(path[:])
        return
    for end in range(start + 1, len(s) + 1):
        if is_palindrome(s, start, end - 1):
            path.append(s[start:end])
            partition_helper(s, end, path, result)
            path.pop()


def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
