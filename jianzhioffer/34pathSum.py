# coding: utf-8
# https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/

from typing import List
from copy import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """dfs, preorder"""
        if not root:
            return []
        self.res = []
        self.pathSum_core(root, sum, [], 0)
        return self.res

    def pathSum_core(self, root, sum, path, cur_sum):
        if not root.left and not root.right:
            if cur_sum + root.val == sum:
                path.append(root.val)
                self.res.append(copy(path))
                path.pop()
        else:
            path.append(root.val)
            cur_sum += root.val
            if root.left:
                self.pathSum_core(root.left, sum, path, cur_sum)
            if root.right:
                self.pathSum_core(root.right, sum, path, cur_sum)
            cur_sum -= root.val
            path.pop()