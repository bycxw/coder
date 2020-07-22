# coding: utf-8
# https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """Copied node connects next to original node. O(n) time complexity. O(1) space complexity."""
        self.clone_node(head)
        self.connect_random(head)
        copied = self.reconnect_node(head)
        return copied

    def clone_node(self, head):
        """connect cloned node next to original node"""
        original = head
        while original:
            cloned = Node(original.val, original.next)
            original.next = cloned
            original = cloned.next

    def connect_random(self, head):
        """connect random pointer with cloned nodes"""
        original = head
        while original:
            cloned = original.next
            if original.random:
                cloned.random = original.random.next
            original = cloned.next

    def reconnect_node(self, head):
        """split original list and cloned list."""
        original = head
        copied = None
        cloned = None
        if original:
            copied = original.next
            cloned = original.next
            original.next = cloned.next
            original = original.next
        while original:
            cloned.next = original.next
            cloned = cloned.next
            original.next = cloned.next
            original = original.next
        return copied

    def copyRandomList2(self, head: 'Node') -> 'Node':
        """use dict. O(n) space complexity"""
        mapping = dict()
        original = head
        copied = None
        if original:
            mapping[original] = Node(original.val)
            copied = mapping[original]
        while original:
            if not original.next:
                mapping[original].next = None
            else:
                if original.next not in mapping:
                    mapping[original.next] = Node(original.next.val)
                mapping[original].next = mapping[original.next]
            if not original.random:
                mapping[original].random = None
            else:
                if original.random not in mapping:
                    mapping[original.random] = Node(original.random.val)
                mapping[original].random = mapping[original.random]
            original = original.next
        return copied
