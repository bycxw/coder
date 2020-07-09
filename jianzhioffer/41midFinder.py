# coding: utf-8
# https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/

from abc import ABCMeta, abstractmethod


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = MinHeap()
        self.maxheap = MaxHeap()

    def addNum(self, num: int) -> None:
        if len(self.maxheap) == 0:
            self.maxheap.insert(num)
        elif len(self.minheap) == len(self.maxheap):
            if self.minheap.top() >= num:
                self.maxheap.insert(num)
            else:
                self.maxheap.insert(self.minheap.pop())
                self.minheap.insert(num)
        else:
            if self.maxheap.top() <= num:
                self.minheap.insert(num)
            else:
                self.minheap.insert(self.maxheap.pop())
                self.maxheap.insert(num)

    def findMedian(self) -> float:
        if len(self.maxheap) == 0:
            raise LookupError("No data.")
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap.top() + self.maxheap.top()) / 2
        else:
            return self.maxheap.top()


class BaseHeap(metaclass=ABCMeta):
    """Base heap"""
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def top(self):
        if not self.heap:
            raise LookupError("empty heap!")
        return self.heap[0]

    def pop(self):
        if not self.heap:
            raise LookupError("empty heap!")
        res = self.top()
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sink()
        return res

    def insert(self, x):
        self.heap.append(x)
        self._swim()

    @abstractmethod
    def _swim(self):
        pass

    @abstractmethod
    def _sink(self):
        pass

class MaxHeap(BaseHeap):
    """Max heap"""
    def __init__(self):
        super().__init__()

    def _swim(self):
        idx = self.__len__() - 1
        parent = ((idx + 1) >> 1) - 1
        while parent >= 0 and self.heap[parent] < self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = ((idx + 1) >> 1) - 1

    def _sink(self):
        idx = 0
        child = (idx << 1) + 1
        while child < self.__len__():
            if child + 1 < self.__len__() and self.heap[child] < self.heap[child + 1]:
                child += 1
            if self.heap[child] > self.heap[idx]:
                self.heap[child], self.heap[idx] = self.heap[idx], self.heap[child]
                idx = child
                child = (idx << 1) + 1
            else:
                break


class MinHeap(BaseHeap):
    """Min heap"""
    def __init__(self):
        super().__init__()

    def _swim(self):
        idx = self.__len__() - 1
        parent = ((idx + 1) >> 1) - 1
        while parent >= 0 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = ((idx + 1) >> 1) - 1

    def _sink(self):
        idx = 0
        child = (idx << 1) + 1
        while child < self.__len__():
            if child + 1 < self.__len__() and self.heap[child] > self.heap[child + 1]:
                child += 1
            if self.heap[child] < self.heap[idx]:
                self.heap[child], self.heap[idx] = self.heap[idx], self.heap[child]
                idx = child
                child = (idx << 1) + 1
            else:
                break

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
