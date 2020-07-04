# coding: utf-8
# https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n < 0:
            raise ("Invalid input: {}, {}".format(x, n))
        if n < 0:
            res = 1 / self.my_pow_core(x, -n)
        else:
            res = self.my_pow_core(x, n)
        return res

    def my_pow_core(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        res = self.my_pow_core(x, n >> 1)
        res *= res
        if n & 1 == 1:
            res *= x
        return res
