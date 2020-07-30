# coding: utf-8
# https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/

from typing import List

class Element:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return str(self.x) + str(other.x) < str(other.x) + str(self.x)

    def __eq__(self, other):
        return str(self.x) + str(other.x) == str(other.x) + str(self.x)

    def __gt__(self, other):
        return str(self.x) + str(other.x) > str(other.x) + str(self.x)

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        if not nums:
            return None
        nums_ = [Element(x) for x in nums]
        nums_ = sorted(nums_)
        res = [str(num.x) for num in nums_]
        return ''.join(res)
