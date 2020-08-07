# coding: utf-8
# https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/

from typing import List

class Solution:
    def twoSum(self, n: int) -> List[float]:
        """f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4) + f(n-5) + f(n-6)"""
        max_value = 6

        def calc_next(count, i):
            res = 0
            for j in range(i - 1, i - max_value - 1, -1):
                if j <= 0:
                    return res
                res += count[j]
            return res
        counts = [[0] * (n * max_value + 1) for _ in range(2)]
        flag = 0
        for i in range(1, max_value + 1):
            counts[0][i] = 1
        cur_n = 2
        while cur_n <= n:
            flag += 1
            for i in range(cur_n, cur_n * max_value + 1):
                counts[flag % 2][i] = calc_next(counts[1 - flag % 2], i)
            cur_n += 1
        prob = [0] * (max_value * n - n + 1)
        total = max_value ** n
        for i in range(n, n * max_value + 1):
            prob[i - n] = counts[flag % 2][i] / total
        return prob
