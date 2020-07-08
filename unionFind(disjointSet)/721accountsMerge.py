# coding: utf-8
# https://leetcode.com/problems/accounts-merge/

from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = []
        self.size = []

    def insert(self):
        self.parent.append(len(self.parent))
        self.size.append(1)

    def find(self, x):
        while self.parent[x] != x:
            # path compression
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        # balanced tree
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """equivalence relation. Union Find"""
        uf = UnionFind()
        email2id = {}  # mapping from email to int which is convenient to implement union-find
        id2name = {}  # mapping from int to name, which is also a mapping from email to name
        for account in accounts:
            for email in account[1:]:
                if email not in email2id:
                    email2id[email] = len(email2id)
                    uf.insert()
                id2name[email2id[email]] = account[0]
                uf.union(email2id[email], email2id[account[1]])
        tmp = defaultdict(list)
        for email, id in email2id.items():
            root = uf.find(id)
            tmp[root].append(email)
        res = []
        for root in tmp:
            res_one = [id2name[root]] + sorted(tmp[root])
            res.append(res_one)
        return res
