# coding: utf-8
# https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """dynamic programming"""
        memo = dict()
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)
            first = i < len(s) and p[j] in [s[i], '.']
            if len(p) - j >= 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)