# coding: utf-8
# https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """post-order traverse"""
        if not root:
            return True
        depth, res = self.isBalancedCore(root)
        return res

    def isBalancedCore(self, root):
        if not root:
            return 0, True
        left_depth, left_res = self.isBalancedCore(root.left)
        right_depth, right_res = self.isBalancedCore(root.right)
        if left_res and right_res and abs(left_depth - right_depth) <= 1:
            return max(left_depth, right_depth) + 1, True
        else:
            return max(left_depth, right_depth) + 1, False
