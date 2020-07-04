# coding: utf-8
# https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/

class Solution:
    def hammingWeight(self, n: int) -> int:
        n &= 0xFFFFFFFF
        cnt = 0
        while n:
            cnt += 1
            n &= n - 1
        return cnt