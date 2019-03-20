from ds.arrays.queue import Queue
from ds.arrays.stack import Stack

"""
Generic NODE class
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.neighbours = list()

"""
Generic Graph class
"""


class Graph:

    def __init__(self, root):
        self.root = root

    def recursive_dfs(self, root=None, visit_data=dict()):

        if not root:
            root = self.root

        print root.data
        visit_data[root] = True
        for neighbour in root.neighbours:
            if not visit_data.get(neighbour):
                self.recursive_dfs(neighbour, visit_data)

    def iterative_dfs(self, root=None):

        if not root:
            root = self.root

        visit_data = dict()
        stack = Stack()
        stack.push(root)
        visit_data[root] = True

        while not stack.is_empty():
            curr_node = stack.pop()
            print curr_node.data
            for neighbour in curr_node.neighbours:
                if not visit_data.get(neighbour):
                    stack.push(neighbour)
                    visit_data[neighbour] = True

    def bfs(self, root=None):

        if not root:
            root = self.root

        visit_data = dict()
        queue = Queue()
        queue.insert(root)
        visit_data[root] = True

        while not queue.is_empty():
            curr_node = queue.delete()
            print curr_node.data
            for neighbour in curr_node.neighbours:
                if not visit_data.get(neighbour):
                    queue.insert(neighbour)
                    visit_data[neighbour] = True