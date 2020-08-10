# coding: utf-8
# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def insert_head(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        self.length += 1

    def remove_tail(self):
        last = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.length -= 1
        return last

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.length -= 1


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.cache = DoubleLinkedList()

    def put(self, key: int, value: int) -> None:
        new = Node(key, value)
        if key in self.mapping:
            self.cache.remove(self.mapping[key])
        elif self.cache.length == self.capacity:
            last = self.cache.remove_tail()
            self.mapping.pop(last.key)
        self.cache.insert_head(new)
        self.mapping[key] = new

    def get(self, key) -> int:
        if key in self.mapping:
            self.put(key, self.mapping[key].value)
            return self.mapping[key].value
        else:
            return -1

