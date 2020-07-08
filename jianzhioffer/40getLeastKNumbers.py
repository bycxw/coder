# coding: utf-8
# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """quick sort"""
        if k <= 0:
            return []
        if len(arr) <= k:
            return arr
        def argmid(arr, left, mid, right):
            if (arr[left] - arr[mid]) * (arr[mid] - arr[right]) >= 0:
                return mid
            elif (arr[mid] - arr[left]) * (arr[left] - arr[right]) >= 0:
                return left
            else:
                return right

        def partition(arr, left, right):
            if left >= right:
                return left
            mid = left + (right - left) >> 1
            pivet_idx = argmid(arr, left, mid, right)
            arr[pivet_idx], arr[left] = arr[left], arr[pivet_idx]
            pivet = arr[left]
            while left < right:
                while left < right and arr[right] > pivet:
                    right -= 1
                arr[left] = arr[right]
                while left < right and arr[left] <= pivet:
                    left += 1
                arr[right] = arr[left]
            arr[left] = pivet
            return left
        left, right = 0, len(arr) - 1
        pivet_idx = partition(arr, left, right)
        while pivet_idx + 1 != k:
            if pivet_idx + 1 > k:
                right = pivet_idx - 1
                pivet_idx = partition(arr, left, right)
            else:
                left = pivet_idx + 1
                pivet_idx = partition(arr, left, right)
        return arr[:pivet_idx + 1]


    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        """heap"""
        if k <= 0:
            return []
        if len(arr) <= k:
            return arr

        def sink(heap):
            idx = 0
            next_idx = (idx << 1) + 1
            while next_idx < len(heap):
                next_idx = (idx << 1) + 1
                if next_idx + 1 < len(heap) and heap[next_idx + 1] > heap[next_idx]:
                    next_idx += 1
                if heap[idx] < heap[next_idx]:
                    heap[idx], heap[next_idx] = heap[next_idx], heap[idx]
                    idx = next_idx
                    next_idx = (idx << 1) + 1
                else:
                    break

        def swim(heap):
            idx = len(heap) - 1
            next_idx = ((idx + 1) >> 1) - 1
            while next_idx >= 0 and heap[idx] > heap[next_idx]:
                heap[idx], heap[next_idx] = heap[next_idx], heap[idx]
                idx = next_idx
                next_idx = ((idx + 1) >> 1) - 1
            
        heap = []
        for num in arr:
            if len(heap) < k:
                heap.append(num)
                swim(heap)
            elif heap[0] > num:
                heap[0] = num
                sink(heap)
        return heap

