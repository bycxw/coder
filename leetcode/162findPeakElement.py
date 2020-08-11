# coding: utf-8
# https://leetcode.com/problems/find-peak-element/

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """binary search, O(logn) time complexity."""
        if not nums:
            return -1

        def findPeakElementCore(left, right):
            if left == right:
                return left
            if right - left == 1:
                if nums[right] > nums[left]:
                    return right
                else:
                    return left
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid - 1]:
                return findPeakElementCore(left, mid - 1)
            elif nums[mid] < nums[mid + 1]:
                return findPeakElementCore(mid + 1, right)
            else:
                return mid

        res = findPeakElementCore(0, len(nums) - 1)
        return res
