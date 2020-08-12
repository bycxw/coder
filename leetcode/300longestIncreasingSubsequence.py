# coding: utf-8
# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """dp"""
        if not nums:
            return 0
        memo = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)
        return max(memo)
