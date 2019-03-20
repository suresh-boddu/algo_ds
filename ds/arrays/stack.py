
"""
Generic Stack data structure
"""

import array


class Stack:
    """
    Stack data structure implementation based of list
    """

    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(len(self.stack) - 1)

    def top(self):
        return self.stack[len(self.stack) - 1]

    def display(self):
        print self.stack

    def is_empty(self):
        return len(self.stack) == 0


class AStack:
    """
    Stack data structure implementation based of array
    """

    def __init__(self):
        self.stack = array.array('i')

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]

    def display(self):
        print self.stack

    def is_empty(self):
        return len(self.stack) == 0
