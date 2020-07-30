# coding: utf-8
# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/

class Solution:
    def translateNum(self, num: int) -> int:
        """dynamic programming"""
        if num < 0:
            return 0
        num_ = str(num)
        memo = [1, 1]
        for i in range(1, len(num_)):
            if 26 > int(num_[i - 1] + num_[i]) > 9:
                memo.append(memo[-1] + memo[-2])
            else:
                memo.append(memo[-1])
        return memo[-1]
