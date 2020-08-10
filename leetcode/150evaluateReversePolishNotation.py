# coding: utf-8
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        def eval_exp(exp):
            res = eval(exp)
            if res > 0:
                res = math.floor(res)
            else:
                res = math.ceil(res)
            return str(res)
        operators = {'+', '-', '*', '/'}
        tmp = []
        for e in tokens:
            if e not in operators:
                tmp.append(e)
            else:
                b = tmp.pop()
                a = tmp.pop()
                tmp.append(eval_exp(a + e + b))
        return int(tmp[0])
