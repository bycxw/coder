# coding: utf-8
# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/

from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        """Level order using a queue. BFS"""
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            size = len(q)
            while size > 0:
                size -= 1
                node = q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """Level order using a queue. BFS"""
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            res.append([])
            size = len(q)
            while size > 0:
                size -= 1
                node = q.popleft()
                res[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        """zigzag level order. Use two stacks."""
        if not root:
            return []
        stacks = [[], []]
        stacks[0].append(root)
        current = 0
        res = []
        while stacks[current]:
            size = len(stacks[current])
            res.append([])
            while size > 0:
                size -= 1
                node = stacks[current].pop()
                res[-1].append(node.val)
                if current:
                    if node.right:
                        stacks[1-current].append(node.right)
                    if node.left:
                        stacks[1-current].append(node.left)
                else:
                    if node.left:
                        stacks[1-current].append(node.left)
                    if node.right:
                        stacks[1-current].append(node.right)
            current = 1- current
        return res