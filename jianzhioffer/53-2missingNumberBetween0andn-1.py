# coding: utf-8
# https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """missing number is the first number that is not equal to its index. binary search."""
        if not nums:
            return 0
        res = self.find_first(nums, 0, len(nums) - 1)
        return res

    def find_first(self, nums, start, end):
        """find first element that isn't equal to its index. binary search"""
        if start > end:  # None isn't equal to its index.
            return len(nums)
        mid = start + (end - start) // 2
        if nums[mid] != mid:
            if mid > 0 and nums[mid - 1] == mid - 1 or mid == 0:
                return mid
            end = mid - 1
        else:
            start = mid + 1
        return self.find_first(nums, start, end)