# coding: utf-8
# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

from collections import deque

class CQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def appendTail(self, value: int) -> None:
        self.inStack.append(value)

    def deleteHead(self) -> int:
        if self.outStack:
            return self.outStack.pop()
        else:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            if self.outStack:
                return self.outStack.pop()
            else:
                return -1

class CQueue2:

    def __init__(self):
        self.inStack = deque()
        self.outStack = deque()

    def appendTail(self, value: int) -> None:
        self.inStack.append(value)

    def deleteHead(self) -> int:
        if self.outStack:
            return self.outStack.pop()
        else:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            if self.outStack:
                return self.outStack.pop()
            else:
                return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()