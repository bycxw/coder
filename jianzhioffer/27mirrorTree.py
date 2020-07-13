# coding: utf-8
# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/

# invert binary tree

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # recursive
        if not root or not root.left and not root.right:
            return root
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root

    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        # iterative
        if not root or not root.left and not root.right:
            return root
        q = [root]
        while q:
            tmp = q.pop()
            while tmp:
                tmp.left, tmp.right = tmp.right, tmp.left
                if tmp.right:
                    q.append(tmp.right)
                tmp = tmp.left
        return root
