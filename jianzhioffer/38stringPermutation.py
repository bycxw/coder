# coding: utf-8
# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/


from typing import List

class Solution:
    """backtrack. divide and conquer"""
    def permutation(self, s: str) -> List[str]:
        if not s:
            return ['']
        res = []
        for i, c in enumerate(s):
            s_rest = s[:i] + s[i + 1:]
            res.extend([c + res_one for res_one in self.permutation(s_rest)])
        return list(set(res))

    def permutation2(self, s):
        visited = [False] * len(s)
        path = []
        s_ = sorted(s)
        self.res = []
        self.permutation_core(s_, visited, path)
        return self.res

    def permutation_core(self, s, visited, path):
        if len(path) == len(s):
            self.res.append(''.join(path))
        for i in range(len(s)):
            if visited[i] or i > 0 and s[i] == s[i - 1] and not visited[i - 1]:
                continue
            visited[i] = True
            path.append(s[i])
            self.permutation_core(s, visited, path)
            path.pop()
            visited[i] = False
