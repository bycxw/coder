# coding: utf-8
# https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """binary search, find first and last target in list. O(logn) time complexity."""
        if not nums:
            return 0
        first = self.find_first(nums, target, 0, len(nums) - 1)
        if first == -1:
            return 0
        last = self.find_last(nums, target, 0, len(nums) - 1)
        return last - first + 1

    def find_first(self, nums, target, begin, end):
        """binary search, find first target"""
        if begin > end:  # target not in nums
            return -1
        mid = begin + (end - begin) // 2
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] != target or mid == 0:
                return mid
            end = mid - 1
        elif nums[mid] < target:
            begin = mid + 1
        else:
            end = mid - 1
        return self.find_first(nums, target, begin, end)

    def find_last(self, nums, target, begin, end):
        """binary search, find last target"""
        if begin > end:  # target not in nums
            return -1
        mid = begin + (end - begin) // 2
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] != target or mid == len(nums) - 1:
                return mid
            begin = mid + 1
        elif nums[mid] < target:
            begin = mid + 1
        else:
            end = mid - 1
        return self.find_last(nums, target, begin, end)
