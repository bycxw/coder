# coding: utf-8
# https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/submissions/

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        res = []
        pnode = head
        while pnode:
            res.append(pnode.val)
            pnode = pnode.next
        res.reverse()
        return res

    def reversePrint2(self, head: ListNode) -> List[int]:
        if not head:
            return []
        res = self.reversePrint2(head.next)
        res.append(head.val)
        return res
