# coding: utf-8
# https://leetcode.com/problems/fizz-buzz/

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n < 1:
            return []
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                one = 'Fizz'
            else:
                one = ''
            if i % 5 == 0:
                two = 'Buzz'
            else:
                two = ''
            if one + two != '':
                res.append(one + two)
            else:
                res.append(str(i))
        return res

