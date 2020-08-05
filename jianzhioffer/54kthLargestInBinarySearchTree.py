# coding: utf-8
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """Inorder traverse from right to left."""
        self.res = []
        self.flag = False
        self.kth_largest_core(root, k)
        return self.res[k - 1]

    def kth_largest_core(self, root, k):
        if root.right:
           self.kth_largest_core(root.right, k)
        if not self.flag:
            self.res.append(root.val)
            if len(self.res) == k:
                self.flag = True
                return
        if not self.flag:
            if root.left:
                self.kth_largest_core(root.left, k)