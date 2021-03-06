# coding: utf-8
# https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/



class MinStack:
    """return minimum element in stack with O(1) time complexity. Use a auxiliary stack."""
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        if not self.stack:
            raise Exception("Empty stack")
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise Exception("Empty stack")
        return self.stack[-1]

    def min(self) -> int:
        if not self.stack:
            raise Exception("Empty stack")
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()