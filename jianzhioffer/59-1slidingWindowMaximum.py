# coding: utf-8
# https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        index = deque()
        for i in range(k):
            while len(index) > 0 and nums[i] >= nums[index[-1]]:
                index.pop()
            index.append(i)
        res = [nums[index[0]]]
        for i in range(k, len(nums)):
            while len(index) > 0 and nums[i] >= nums[index[-1]]:
                index.pop()
            index.append(i)
            if index[0] <= i - k:
                index.popleft()
            res.append(nums[index[0]])
        return res
