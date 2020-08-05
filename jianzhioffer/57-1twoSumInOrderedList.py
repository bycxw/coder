# coding: utf-8
# https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """two pointers."""
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            if nums[p1] + nums[p2] < target:
                p1 += 1
            elif nums[p1] + nums[p2] > target:
                p2 -= 1
            else:
                return [nums[p1], nums[p2]]