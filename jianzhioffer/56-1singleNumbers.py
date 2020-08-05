# coding: utf-8
# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/

from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        """XOR"""
        res = 0
        for num in nums:
            res ^= num
        s = str(bin(res))
        idx = len(s) - s.index('1')
        nums_1 = [x for x in nums if idx < len(str(bin(x))) and str(bin(x))[-idx] == '1']
        nums_2 = [x for x in nums if idx >= len(str(bin(x))) or str(bin(x))[-idx] != '1']
        num_1 = 0
        for num in nums_1:
            num_1 ^= num
        num_2 = 0
        for num in nums_2:
            num_2 ^= num
        return [num_1, num_2]