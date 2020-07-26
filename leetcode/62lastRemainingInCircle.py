# coding: utf-8
# https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        """simulate the circle with a linked list. time exceed limit."""
        if n <= 1:
            return n - 1
        head = ListNode(0)
        cur = head
        for i in range(1, n):
            cur.next = ListNode(i)
            cur = cur.next
        cur.next = head
        pre = cur
        cur = head
        while cur.next != cur:
            pre, cur = self.drop_one(pre, cur, m)
        return cur.val


    def drop_one(self, pre, head, m):
        for i in range(m - 1):
            pre = pre.next
            head = head.next
        pre.next = head.next
        head = head.next
        return pre, head

    def lastRemaining2(self, n: int, m: int) -> int:
        """
        https://blog.csdn.net/Xu_JL1997/article/details/88558812
        Josephuse dp
        f(n,m)=0,  n=1
        f(n,m)=(f(n−1,m)+m)%n  , n>1
        """
        if n <= 1:
            return 0
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last
