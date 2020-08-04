# coding: utf-8
# https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """merge sort"""
        if not nums:
            return 0
        cnt = 0
        cnt = self.merge_cnt(nums, 0, len(nums) - 1, cnt)
        return cnt

    def merge_cnt(self, nums, left, right, cnt) -> int:
        if left >= right:
            return cnt
        mid = left + (right - left) // 2 + 1
        cnt = self.merge_cnt(nums, left, mid - 1, cnt)
        cnt = self.merge_cnt(nums, mid, right, cnt)
        copy = [0] * (right - left + 1)
        i = mid - 1
        j = right
        end = len(copy) - 1
        while i >= left and j >= mid:
            if nums[i] > nums[j]:
                copy[end] = nums[i]
                end -= 1
                i -= 1
                cnt += (j - mid + 1)
            else:
                copy[end] = nums[j]
                end -= 1
                j -= 1
        if i >= left:
            end += 1
            while end < len(copy):
                nums[end + left] = copy[end]
                end += 1
        elif j >= mid:
            while j >= mid:
                copy[end] = nums[j]
                end -= 1
                j -= 1
            for end in range(len(copy)):
                nums[end + left] = copy[end]
        return cnt
