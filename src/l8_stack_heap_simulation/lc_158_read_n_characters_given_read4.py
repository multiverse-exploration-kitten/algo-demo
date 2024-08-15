# The read4 API is already defined for you.


from collections import deque
from typing import List


def read4(buf4: List[str]) -> int:
    pass


class Solution:
    def __init__(
        self,
    ):
        self.q = deque([])

    def read(self, buf: List[str], n: int) -> int:
        for i in range(n):
            buf[i] = ""

        tot = n

        if n <= len(self.q):
            while n > 0:
                item = self.q.popleft()
                if item is not None:
                    print(item)
                    buf[tot - n] = item
                n -= 1
        else:
            while self.q:
                item = self.q.popleft()
                if item is not None:
                    buf[tot - n] = item
                n -= 1

            while n > 0:
                if len(self.q) == 0:
                    tmp = [None for _ in range(4)]
                    read4(tmp)
                    for t in tmp:
                        self.q.append(t)

                item = self.q.popleft()

                if item is not None:
                    print(item)
                    buf[tot - n] = item

                n -= 1

        return tot
