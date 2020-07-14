# coding: utf-8
# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/


from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """Use a auxiliary stack."""
        if len(pushed) != len(popped):
            return False
        stack = []
        idx = 0
        for num in popped:
            while not stack or stack[-1] != num:
                if idx >= len(popped):
                    return False
                stack.append(pushed[idx])
                idx += 1
            stack.pop()
        return True
