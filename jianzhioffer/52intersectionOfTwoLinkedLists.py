# coding: utf-8
# https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """O(m + n) time complexity."""
        p = headA
        cntA = 0
        while p:
            p = p.next
            cntA += 1
        p = headB
        cntB = 0
        while p:
            p = p.next
            cntB += 1
        if cntA > cntB:
            p1 = headA
            while cntA > cntB:
                p1 = p1.next
                cntA -= 1
            p2 = headB
        else:
            p1 = headB
            while cntB > cntA:
                p1 = p1.next
                cntB -= 1
            p2 = headA
        while p1:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None
