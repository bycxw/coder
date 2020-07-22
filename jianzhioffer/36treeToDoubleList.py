# coding: utf-8
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/



# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """recursive"""
        if not root:
            return root
        head, tail = self.treeToDoublyList_core(root)
        head.left = tail
        tail.right = head
        return head

    def treeToDoublyList_core(self, root):
        head = root
        if root.left:
            head, tail_ = self.treeToDoublyList_core(root.left)
            root.left = tail_
            tail_.right = root
        tail = root
        if root.right:
            head_, tail = self.treeToDoublyList_core(root.right)
            root.right = head_
            head_.left = root
        return head, tail

    def treeToDoubleList2(self, root: 'Node') -> 'Node':
        """inorder traverse"""
        if not root:
            return root
        self.res = []
        self.inorder(root)
        for i in range(len(self.res)):
            self.res[i].right, self.res[(i + 1) % len(self.res)].left = self.res[(i + 1) % len(self.res)], self.res[i]
        return self.res[0]

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        self.res.append(root)
        if root.right:
            self.inorder(root.right)
