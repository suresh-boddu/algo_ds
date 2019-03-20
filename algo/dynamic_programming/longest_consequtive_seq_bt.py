"""
Given a Binary Tree find the length of the longest path which comprises of nodes with
consecutive values in increasing order. Every node is considered as a path of length 1.

"""

from ds.trees.tree import Node
from ds.trees.tree import Tree


def find_lcs(node):

    if not node:
        return 0

    if not (node.left or node.right):
        return 1

    left_lcs = right_lcs = 0

    if node.left:
        left_lcs = find_lcs(node.left) + (1 if (node.data < node.left.data) else 0)
    if node.right:
        right_lcs = find_lcs(node.right) + (1 if (node.data < node.right.data) else 0)

    return max(left_lcs, right_lcs)

def main():
    node5 = Node(5, None, None)
    node4 = Node(4, None, None)
    node3 = Node(3, node5, None)
    node2 = Node(2, None, node4)
    node1 = Node(1, node2, node3)

    lcs = find_lcs(node3)
    print("lcs of node: %s is %s"%(node3.data, lcs))

    lcs = find_lcs(node4)
    print("lcs of node: %s is %s" % (node4.data, lcs))

    lcs = find_lcs(node1)
    print("lcs of node: %s is %s" % (node1.data, lcs))


if __name__ == '__main__':
    main()
