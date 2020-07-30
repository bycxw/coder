# coding: utf-8
# https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/

from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """dynamiic programming"""
        if not grid or not grid[0]:
            return 0
        memo = [[0] * len(grid[0]) for _ in range(len(grid))]
        memo[0][0] = grid[0][0]
        for i in range(1, len(grid[0])):
            memo[0][i] = memo[0][i - 1] + grid[0][i]
        for i in range(1, len(grid)):
            memo[i][0] = memo[i - 1][0] + grid[i][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1]) + grid[i][j]
        return memo[-1][-1]