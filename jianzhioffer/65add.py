# coding: utf-8
# https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/

import ctypes


class Solution:
    def add(self, a: int, b: int) -> int:
        """add without + - * /.    with bit operation"""
        a = ctypes.c_int32(a).value
        b = ctypes.c_int32(b).value
        while b != 0:
            sum = ctypes.c_int32(a ^ b).value
            carry = ctypes.c_int32((a & b) << 1).value
            a = sum
            b = carry
        return a