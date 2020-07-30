# coding: utf-8
# https://leetcode-cn.com/problems/chou-shu-lcof/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """dynamic programming"""
        if n <= 0:
            return 0
        memo = [1, ]
        factor2_idx = factor3_idx = factor5_idx = 0
        while len(memo) < n:
            next_ugly_num = min(memo[factor2_idx] * 2, memo[factor3_idx] * 3, memo[factor5_idx] * 5)
            memo.append(next_ugly_num)
            while memo[factor2_idx] * 2 <= next_ugly_num:
                factor2_idx += 1
            while memo[factor3_idx] * 3 <= next_ugly_num:
                factor3_idx += 1
            while memo[factor5_idx] * 5 <= next_ugly_num:
                factor5_idx += 1
        return memo[-1]
