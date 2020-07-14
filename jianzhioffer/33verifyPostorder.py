# coding: utf-8
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/

from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """recursive. divide and conquer"""
        if not postorder:
            return True
        i = 0
        while i < len(postorder) - 1:
            if postorder[i] > postorder[-1]:
                break
            i += 1
        for j in range(len(postorder) - 2, i, -1):
            if postorder[j] <= postorder[-1]:
                return False
        return self.verifyPostorder(postorder[:i]) and self.verifyPostorder(postorder[i: -1])
