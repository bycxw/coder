# coding: utf-8
# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

from typing import List
import unittest

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for num in nums:
            if num >= len(nums) or num < 0:
                return -1
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    tmp = nums[i]
                    nums[i], nums[tmp] = nums[tmp], nums[i]
        return -1

    def findRepeatNumber2(self, nums: List[int]) -> int:
        # """不改变原始数组"""
        if not nums:
            return -1
        for num in nums:
            if num <= 0 or num >= len(nums):
                return -1
        begin, end = 1, len(nums) - 1
        while end >= begin:
            middle = begin + (end - begin) // 2
            count = self.count_range(nums, begin, middle)
            if end == begin:
                if count > 1:
                    return begin
                break
            if count > middle - begin + 1:
                end = middle
            else:
                begin = middle + 1
        return -1

    def count_range(self, nums, begin, end):
        if not nums:
            return 0
        cnt = 0
        for num in nums:
            if num >= begin and num <= end:
                cnt += 1
        return cnt




class TestSolution(unittest.TestCase):
    def test_case1(self):
        case = [2, 3, 1, 2, 5, 3]
        self.assertIn(Solution().findRepeatNumber2(case), [2, 3])

    def test_case2(self):
        case = [2, 1, 3]
        self.assertEqual(Solution().findRepeatNumber2(case), -1)

    def test_case3(self):
        case = []
        self.assertEqual(Solution().findRepeatNumber2(case), -1)

    def test_case4(self):
        case = [-2, 3]
        self.assertEqual(Solution().findRepeatNumber2(case), -1)

    
if __name__ == "__main__":
    unittest.main()