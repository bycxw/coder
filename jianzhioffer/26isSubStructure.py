# coding: utf-8
# https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/

# If tree B is sub-structure of tree A.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        res = False
        if A and B:
            if A.val == B.val:
                res = self.is_identical(A, B)
            if not res:
                res = self.isSubStructure(A.left, B)
            if not res:
                res = self.isSubStructure(A.right, B)
        return res

    def is_identical(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.is_identical(A.left, B.left) and self.is_identical(A.right, B.right)
