# coding: utf-8
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """in-order traverse."""
        res = [k, ]

        def kthSmallestCore(root, res):
            if len(res) > 1:
                return
            if root.left:
                kthSmallestCore(root.left, res)
            res[0] -= 1
            if res[0] == 0:
                res.append(root.val)
                return
            if root.right:
                kthSmallestCore(root.right, res)

        kthSmallestCore(root, res)
        return res[1]
