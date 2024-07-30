from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, nxt: Optional["ListNode"] = None):
        self.val = val
        self.nxt = nxt


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge_two_lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None

    def merge_two_lists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = point = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                point.nxt = l1
                l1 = l1.nxt
            else:
                point.nxt = l2
                l2 = l2.nxt
            point = point.nxt

        if not l1:
            point.next = l2
        else:
            point.next = l1

        return head.nxt
