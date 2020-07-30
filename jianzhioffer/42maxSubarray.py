# coding: utf-8
# https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """dynamic programming"""
        if not nums:
            return 0
        memo = nums[:1]
        for i in range(1, len(nums)):
            memo.append(max(nums[i] + memo[i - 1], nums[i]))
        return max(memo)
