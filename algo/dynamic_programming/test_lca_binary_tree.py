import unittest
from ds.trees.tree import Node
from ds.trees.tree import Tree
from algo.dynamic_programming.lca_binary_tree import find_lca


class TestLCABinaryTree(unittest.TestCase):

    def test_something(self):
        node5 = Node(5, None, None)
        node4 = Node(4, None, None)
        node3 = Node(3, node5, None)
        node2 = Node(2, None, node4)
        node1 = Node(1, node2, node3)

        tree = Tree(node1)
        lca = find_lca(tree.root, 4, 5)
        self.assertEqual(1, lca.data if lca else None)

        lca = find_lca(tree.root, 2, 3)
        self.assertEqual(1, lca.data if lca else None)

        lca = find_lca(tree.root, 2, 4)
        self.assertEqual(2, lca.data if lca else None)

        lca = find_lca(tree.root, 3, 5)
        self.assertEqual(3, lca.data if lca else None)

        lca = find_lca(tree.root, 5, 6)
        self.assertEqual(5, lca.data if lca else None)

        lca = find_lca(tree.root, 6, 7)
        self.assertEqual(None, lca.data if lca else None)


if __name__ == '__main__':
    unittest.main()
