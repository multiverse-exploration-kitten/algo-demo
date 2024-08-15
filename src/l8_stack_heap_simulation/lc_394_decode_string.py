class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        number = 0

        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == "[":
                stack.append(number)
                number = 0
            else:
                if c == "]":
                    tmp = self.pop_stack(stack)
                    occurrence = int(stack.pop())
                    for _ in range(occurrence):
                        stack.append(tmp)
                else:
                    stack.append(c)

        return self.pop_stack(stack)

    def pop_stack(self, stack):
        buffer_stack = []

        while stack and isinstance(stack[-1], str):
            buffer_stack.append(stack.pop())

        s = []
        while buffer_stack:
            s.append(buffer_stack.pop())

        return "".join(s)
