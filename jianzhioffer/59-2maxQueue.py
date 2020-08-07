# coding: utf-8
# https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/

from collections import deque

class MaxQueue:
    """queue with max method. O(1) time complexity."""
    def __init__(self):
        self.queue = deque()
        self.max_q = deque()
        self.idx = 0

    def max_value(self) -> int:
        if len(self.max_q) == 0:
            return -1
        return self.max_q[0][0]


    def push_back(self, value: int) -> None:
        while len(self.max_q) > 0 and value >= self.max_q[-1][0]:
            self.max_q.pop()
        self.queue.append((value, self.idx))
        self.max_q.append((value, self.idx))
        self.idx += 1

    def pop_front(self) -> int:
        if len(self.max_q) == 0:
            return -1
        if self.max_q[0][1] == self.queue[0][1]:
            self.max_q.popleft()
        return self.queue.popleft()[0]



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()