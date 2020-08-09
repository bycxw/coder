# coding: utf-8
# https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/

from copy import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """dfs, find path from root to p and q."""
        def dfs(root, node, path):
            if root == node:
                return copy(path)
            if root.left:
                path.append(root.left)
                res = dfs(root.left, node, path)
                path.pop()
                if res:
                    return res
            if root.right:
                path.append(root.right)
                res = dfs(root.right, node, path)
                path.pop()
                if res:
                    return res
            return None
        path_p = dfs(root, p, [root,])
        path_q = dfs(root, q, [root,])
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i] != path_q[i]:
                return path_p[i - 1]
        if len(path_p) < len(path_q):
            return path_p[-1]
        else:
            return path_q[-1]
