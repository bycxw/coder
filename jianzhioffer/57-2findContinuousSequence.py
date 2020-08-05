# coding: utf-8
# https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/


from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """small, big, two pointers"""
        if target < 2:
            return []
        res = []
        small, big, cur_sum = 1, 2, 3
        while small <= target // 2:
            if cur_sum == target:
                res.append(list(range(small, big + 1)))
                big += 1
            elif cur_sum < target:
                big += 1
                cur_sum += big
            else:
                cur_sum -= small
                small += 1
        return res
