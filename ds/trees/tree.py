"""
Generic NODE class
"""
from ds.arrays.queue import Queue

class Node:

    left = None
    right = None
    data = None

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

"""
Generic TREE class
"""


class Tree:

    root = None

    def __init__(self, root):
        self.root = root

    def in_order(self, root):
        '''
        In order traversal from the given root.
        :param root:
        :return:
        '''

        if root == None:
            return

        if root.left != None:
            self.in_order(root.left)

        print root.data

        if root.right != None:
            self.in_order(root.right)

    def pre_order(self, root):
        '''
        Pre order traversal from the given root.
        :param root:
        :return:
        '''

        if root == None:
            return

        print root.data

        if root.left != None:
            self.pre_order(root.left)

        if root.right != None:
            self.pre_order(root.right)

    def post_order(self, root):
        '''
        Post order traversal from the given root.
        :param root:
        :return:
        '''

        if root == None:
            return

        if root.left != None:
            self.post_order(root.left)

        if root.right != None:
            self.post_order(root.right)

        print root.data

    def level_order(self, root):
        '''
        Level order traversal from the given root.
        :param root:
        :return:
        '''

        if root == None:
            return

        queue = Queue()
        queue.insert(root)


        while not queue.is_empty():
            curr_node = queue.delete()
            print curr_node.data

            if curr_node.left:
                queue.insert(curr_node.left)

            if curr_node.right:
                queue.insert(curr_node.right)
