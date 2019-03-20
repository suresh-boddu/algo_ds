"""
Generic Queue data structure
"""

import array

class Queue:
    """
    Queue data structure implementation based of list
    """

    def __init__(self):
        self.queue = list()

    def insert(self, item):
        self.queue.append(item)

    def delete(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[len(self.queue) - 1]

    def display(self):
        print self.queue

    def is_empty(self):
        return len(self.queue) == 0


class AQueue:
    """
    Queue data structure implementation based of array
    """

    def __init__(self):
        self.queue = array.array('i')

    def insert(self, item):
        self.queue.append(item)

    def delete(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[len(self.queue) - 1]

    def display(self):
        print self.queue

    def is_empty(self):
        return len(self.queue) == 0
