# Monotonic Stack


def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    return result


# Balanced Parentheses
def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


# Stack with Auxiliary Data Structure
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


# Infix to Postfix Conversion / Expression Evaluation
def calculate(s):
    stack = []
    current_number = 0
    operation = "+"
    s += "+"

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char in "+-*/":
            if operation == "+":
                stack.append(current_number)
            elif operation == "-":
                stack.append(-current_number)
            elif operation == "*":
                stack.append(stack.pop() * current_number)
            elif operation == "/":
                stack.append(int(stack.pop() / current_number))

            operation = char
            current_number = 0

    return sum(stack)
