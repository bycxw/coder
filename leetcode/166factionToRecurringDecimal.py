# coding: utf-8
# https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """recursion"""
        sgn = lambda x: 1 if x > 0 else -1 if x < 0 else 0
        if sgn(numerator) * sgn(denominator) == -1:
            pre = '-'
        else:
            pre = ''
        memo = {}
        def fractionToDecimalCore(a, b, res):
            if a == 0:
                return -1
            if a in memo:
                return memo[a]
            else:
                memo[a] = len(res)
            p, q = divmod(a, b)
            res.append(str(p))
            q *= 10
            fractionToDecimalCore(q, b, res)
        res = []
        p, q = divmod(abs(numerator), abs(denominator))
        if q == 0:
            return pre + str(p)
        q *= 10
        index = fractionToDecimalCore(q, abs(denominator), res)
        if index == -1:
            return pre + str(p) + '.' + ''.join(res)
        else:
            return pre + str(p) + '.' + ''.join(res[:index]) + '(' + ''.join(res[index:]) + ')'


