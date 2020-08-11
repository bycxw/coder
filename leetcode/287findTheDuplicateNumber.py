# coding: utf-8
# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """same with linked list with circle. O(n) time complexity. O(1) space complexity."""
        if not nums:
            return -1
        fast = slow = 0
        fast = nums[nums[fast]]
        slow = nums[slow]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = slow[slow]
        return slow
