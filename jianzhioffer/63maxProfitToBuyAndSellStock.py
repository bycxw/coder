# coding: utf-8
# https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """dp"""
        if not prices or len(prices) < 2:
            return 0
        dp = [[0, 0] for _ in  range(len(prices))]
        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i - 1][0], prices[i] + dp[i - 1][1])
                dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        """dp, O(1) space complexity."""
        if not prices or len(prices) < 2:
            return 0
        dp_0 = 0
        dp_1 = -prices[0]
        for i in range(1, len(prices)):
            dp_0 = max(dp_0, prices[i] + dp_1)
            dp_1 = max(dp_1, -prices[i])
        return dp_0
