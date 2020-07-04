# coding: utf-8
# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/

from collections import deque

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if m <= 0 or n <= 0:
            return 0
        self.m, self.n = m, n
        self.cnt = 0
        self.visited = [[False] * n for _ in range(m)]
        self.dfs(0, 0, k)
        return self.cnt

    def dfs(self, row, col, k):
        if not self.valid(row, col, k) or self.visited[row][col]:
            return
        self.cnt += 1
        self.visited[row][col] = True
        self.dfs(row + 1, col, k)
        self.dfs(row - 1, col, k)
        self.dfs(row, col + 1, k)
        self.dfs(row, col - 1, k)
    
    def bfs(self, row, col, k):
        q = deque([(row, col)])
        self.visited[row][col] = True
        while q:
            self.cnt += 1
            row, col = q.popleft()
            if self.valid(row + 1, col, k) and not self.visited[row + 1][col]:
                self.visited[row + 1][col] = True
                q.append((row + 1, col))
            if self.valid(row - 1, col, k) and not self.visited[row - 1][col]:
                self.visited[row - 1][col] = True
                q.append((row - 1, col))
            if self.valid(row, col + 1, k) and not self.visited[row][col + 1]:
                self.visited[row][col + 1] = True
                q.append((row, col + 1))
            if self.valid(row, col - 1, k) and not self.visited[row][col - 1]:
                self.visited[row][col - 1] = True
                q.append((row, col - 1))
        


    def valid(self, row, col, k):
        if row < 0 or row >= self.m or col < 0 or col >= self.n:
            return False
        def calcdec(num):
            res = 0
            while num > 0:
                num, remainder = divmod(num, 10)
                res += remainder
            return res
        return calcdec(row) + calcdec(col) <= k
        