# coding: utf-8
# https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """binary search"""
        if not numbers:
            return
        start, end = 0, len(numbers) - 1
        mid = start
        while numbers[start] >= numbers[end]:
            if end - start == 1:
                mid = end
                break
            mid = start + (end - start) // 2
            if numbers[start] == numbers[mid] and numbers[start] == numbers[end]:
                return self.seqSearch(numbers, start, end)
            if numbers[mid] >= numbers[start]:
                start = mid
            else:
                end = mid
        return numbers[mid]

    @staticmethod
    def seqSearch(numbers, start, end):
        res = numbers[start]
        for i in range(start + 1, end):
            res = min(numbers[i], res)
        return res