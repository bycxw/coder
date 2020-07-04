# coding: utf-8
# https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/

class Solution:
    def cuttingRope(self, n: int) -> int:
        """greedy mod"""
        MOD = 1000000007
        if n == 2:
            return 1
        if n == 3:
            return 2
        quotient, remainder = divmod(n, 3)
        if remainder == 0:
            return 3 ** quotient % MOD
        if remainder == 1:
            return 3 ** (quotient - 1) * 4 % MOD
        if remainder == 2:
            return 3 ** quotient * 2 % MOD