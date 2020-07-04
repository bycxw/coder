# coding: utf-8
# https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        if not word:
            return True
        self.visited = [[False] * len(board[0]) for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.has_path(board, row, col, word):
                    return True
        return False
    
    def has_path(self, board, row, col, word):
        if not word:
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or self.visited[row][col]:
            return False
        if board[row][col] == word[0]:
            self.visited[row][col] = True
            res = self.has_path(board, row + 1, col, word[1:]) or self.has_path(board, row - 1, col, word[1:]) \
                or self.has_path(board, row, col + 1, word[1:]) or self.has_path(board, row, col - 1, word[1:])
            self.visited[row][col] = False
            return res