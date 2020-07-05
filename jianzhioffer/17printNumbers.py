# coding: utf-8
# https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/

from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        if n <= 0:
            return []
        self.n = n
        self.res = []
        num = ["0"] * n
        self.backtrack(num, 0)
        return self.res[1:]

    def backtrack(self, num, depth):
        if depth >= self.n:
            self.res.append(int(''.join(num)))
            return
        for c in range(10):
            num[depth] = str(c)
            self.backtrack(num, depth + 1)

    def printNumbers2(self, n: int) -> List[int]:
        if n <= 0:
            return []
        return list(range(1, 10 ** n - 1))