# coding: utf-8
# https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """majority element is median. We can find the len(nums) / 2 th number of ordered array with partition"""
        def partition(low, high):
            while low < high:
                while low < high and nums[low] < nums[high]:
                    high -= 1
                nums[low], nums[high] = nums[high], nums[low]
                while low < high and nums[low] <= nums[high]:
                    low += 1
                nums[low], nums[high] = nums[high], nums[low]
            return low
        low, high = 0, len(nums) - 1
        while True:
            pivet_idx = partition(low, high)
            if pivet_idx < len(nums) // 2:
                low = pivet_idx + 1
            elif pivet_idx > len(nums) // 2:
                high = pivet_idx - 1
            else:
                break
        return nums[pivet_idx]

    def majorityElement2(self, nums: List[int]) -> int:
        """O(n) time complexity."""
        tmp = [0, 0]
        for num in nums:
            if tmp[1] == 0:
                tmp = [num, 1]
            else:
                if num == tmp[0]:
                    tmp[1] += 1
                else:
                    tmp[1] -= 1
        return tmp[0]
