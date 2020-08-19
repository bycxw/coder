# coding: utf-8
# https://leetcode.com/problems/power-of-three/


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3 == 0:
                n /= 3
            else:
                return False
        return n == 1
