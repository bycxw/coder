# coding: utf-8
# https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """dynamic programming"""
        if not s:
            return 0
        last = dict()
        memo = [1, ]
        res = 1
        last[s[0]] = 0
        for i in range(1, len(s)):
            if i - last.get(s[i], -1) > memo[-1]:
                tmp = memo[-1] + 1
                res = max(res, tmp)
                memo.append(tmp)
            else:
                memo.append(i - last.get(s[i], -1))
            last[s[i]] = i
        return res
