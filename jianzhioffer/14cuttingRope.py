# coding: utf-8
# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/

class Solution:
    def cuttingRope(self, n: int) -> int:
        """dynamic planning"""
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [0, 1, 2, 3]
        for i in range(4, n + 1):
            res = i
            for j in range(1, i // 2 + 1):
                res = max(res, dp[j] * dp[i - j])
            dp.append(res)
        return dp[n]


    def cuttingRope2(self, n: int) -> int:
        """greedy"""
        if n == 2:
            return 1
        if n == 3:
            return 2
        quotient, remainder = divmod(n, 3)
        if remainder == 0:
            return 3 ** quotient
        if remainder == 1:
            return 3 ** (quotient - 1) * 4
        if remainder == 2:
            return 3 ** quotient * 2