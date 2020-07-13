# coding: utf-8
# https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # preorder
        if not root or not root.left and not root.right:
            return True
        inorder_val, inorder_right_val = [], []
        inorder_val = self.inorder(root, inorder_val)
        inorder_right_val = self.inorder_right(root, inorder_right_val)
        if len(inorder_val) != len(inorder_right_val):
            return False
        else:
            for i in range(len(inorder_val)):
                if inorder_val[i] != inorder_right_val[i]:
                    return False
        return True

    def inorder(self, root, res):
        if not root:
            res.append(None)
            return res
        res.append(root.val)
        self.inorder(root.left, res)
        self.inorder_right(root.right, res)
        return res

    def inorder_right(self, root, res):
        if not root:
            res.append(None)
            return res
        res.append(root.val)
        self.inorder_right(root.right, res)
        self.inorder(root.left, res)
        return res
