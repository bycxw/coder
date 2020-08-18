# coding: utf-8
# https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """insert listnode."""
        if not head:
            return head
        even = head.next
        if even:
            odd = even.next
            pre_odd = head
        else:
            return head
        while odd and even:
            even.next = odd.next
            odd.next = pre_odd.next
            pre_odd.next = odd
            pre_odd = odd
            even = even.next
            if even:
                odd = even.next
        return head

