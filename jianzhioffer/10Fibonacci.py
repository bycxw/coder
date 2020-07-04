# coding: utf-8
# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

from collections import deque
from math import sqrt
class Solution:
    def fib(self, n: int) -> int:
        """recursion formula"""
        MOD = 1000000007
        if n < 2:
            return n
        cache = deque([0, 1], maxlen=2)
        for _ in range(2, n + 1):
            cache.append((cache[0] + cache[1]) % MOD)
        return cache[1]

    def fib2(self, n: int) -> int:
        """matrix diagonalization, precision problem"""
        MOD = 1000000007
        if n < 2:
            return n
        a = 0.7236067977499788
        b = 0.2763932022500209
        eig1 = (1 + sqrt(5)) / 2 # 1.61803399
        eig2 = (1 - sqrt(5)) / 2 # -0.61803399
        return round(eig1 ** (n-1) * a + eig2 ** (n-1) * b) % MOD