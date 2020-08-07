# coding: utf-8
# https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/

from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        """two auxiliary arrays: left product and right product."""
        if not a:
            return []
        left_prod = [1] * len(a)
        right_prod = [1] * len(a)
        for i in range(1, len(a)):
            left_prod[i] = left_prod[i - 1] * a[i - 1]
            right_prod[len(a) - i - 1] = right_prod[len(a) - i] * a[len(a) - i]
        res = [1] * len(a)
        for i in range(len(a)):
            res[i] = left_prod[i] * right_prod[i]
        return res
