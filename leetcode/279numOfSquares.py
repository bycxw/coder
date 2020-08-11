# coding: utf-8
# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        """dp"""
        if n < 0:
            return 0

        memo = [0, 1, ]
        for i in range(2, n + 1):
            memo.append(i)
            j = 1
            while j * j <= i:
                memo[-1] = min(memo[-1], 1 + memo[n - j * j])
                j += 1
        return memo[-1]

    def numSquares2(self, n: int) -> int:
        """bfs"""
        from collections import deque
        q = deque()
        i = 1
        while i * i <= n:
            remain = n - i * i
            q.append(remain)
            if remain == 0:
                return 1
            i += 1
        res = 1
        while len(q) > 0:
            size = len(q)
            res += 1
            while size > 0:
                size -= 1
                remain = q.popleft()
                i = 1
                while i * i <= remain:
                    remain_ = remain - i * i
                    if remain_ == 0:
                        return res
                    q.append(remain_)
                    i += 1
