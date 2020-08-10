# coding: utf-8
# https://leetcode.com/problems/palindrome-partitioning/

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """dfs, dp"""
        from copy import copy
        memo = {}

        def dfs(index, s, path, res):
            if index == len(s):
                res.append(copy(path))
            else:
                for i in range(index + 1, len(s) + 1):
                    if is_pal(index, i):
                        path.append(s[index :i])
                        dfs(i, s, path, res)
                        path.pop()

        def is_pal(index, i):
            if (index, i) in memo:
                return memo[(index, i)]
            else:
                j, k = index, i - 1
                while j <= k:
                    if s[j] != s[k]:
                        memo[(index, i)] = False
                        return False
                    j += 1
                    k -= 1
                memo[(index, i)] = True
                return True
        res = []
        dfs(0, s, [], res)
        return res
