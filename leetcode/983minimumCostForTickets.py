# coding: utf-8
# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """dynamic programming"""
        if not days:
            return 0
        memo = [0] * (len(days) + 1)
        for i in range(len(days)):
            index = [i - 1, -1, -1]
            for j in range(i - 1, -1, -1):
                if days[i] - days[j] > 6 and index[1] < 0:
                    index[1] = j
                if days[i] - days[j] > 29 and index[2] < 0:
                    index[2] = j
            memo[i] = min(memo[index[0]] + costs[0], memo[index[1]] + costs[1], memo[index[2]] + costs[2])
        return memo[-2]
