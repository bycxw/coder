# coding: utf-8
# https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/

from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        """sort"""
        nums_ = sorted(nums)
        zero_cnt = nums_.count(0)
        gap = 0
        for i in range(zero_cnt, len(nums) - 1):
            if nums_[i + 1] == nums_[i]:
                return False
            gap += nums_[i + 1] - nums_[i] - 1
        return gap <= zero_cnt
