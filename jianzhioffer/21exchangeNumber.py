# coding: utf-8
# https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not bool(nums):
            return []
        def func(num):
            return num & 1 == 1
        return self.exchange_core(nums, func)

    def exchange_core(self, nums, func):
        """start pointer. end pointer"""
        first, second  = 0, len(nums) - 1
        while first < second:
            while first < second and func(nums[first]):
                first += 1
            while first < second and not func(nums[second]):
                second -= 1
            if first < second:
                nums[first], nums[second] = nums[second], nums[first]
        return nums

    def exchange_core2(self, nums, func):
        """fast pointer. slow pointer"""
        slow, fast = 0, 0
        while fast < len(nums):
            if func(nums[fast]):
                if slow != fast:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums