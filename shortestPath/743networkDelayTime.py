# coding: utf-8
# https://leetcode.com/problems/network-delay-time/
# shortest path

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """dijkstra"""
        t_m = defaultdict(dict)
        for u, v, t in times:
            t_m[u][v] = t
        for i in range(1, N + 1):
            t_m[i][i] = 0
        dist = [t_m[K][i] if i in t_m[K] else float('inf') for i in range(1, N + 1)]
        heap = [(0, K)]
        s = set([K])
        while heap:
            time, cur = heapq.heappop(heap)
            if time == float('inf'):
                break
            s.add(cur)
            heap = []
            for i in range(1, N + 1):
                if i in t_m[cur] and i not in s:
                    dist[i - 1] = min(dist[i - 1], t_m[cur][i] + dist[cur - 1])
                if i not in s:
                    heapq.heappush(heap, (dist[i - 1], i))
        if len(s) < N:
            return - 1
        return max(dist)