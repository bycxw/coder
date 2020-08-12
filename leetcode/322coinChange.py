# coding: utf-8
# https://leetcode.com/problems/coin-change/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """dynamic programming"""
        memo = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i], memo[i - coin] + 1)
        if memo[-1] == float('inf'):
            return -1
        return memo[-1]
