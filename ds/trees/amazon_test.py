class Node:

    left = None
    right = None
    data = None

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class Tree:

    root = None

    def __init__(self, root):
        self.root = root


def find_lca(node, key1, key2):

    if not node:
        return

    if node.data == key1 or node.data == key2:
        return node

    lca_left = find_lca(node.left, key1, key2)
    lca_right = find_lca(node.right, key1, key2)

    if lca_left and lca_right:
        return node

    return lca_left if lca_left else lca_right


def main():
    node5 = Node(5, None, None)
    node4 = Node(4, None, node5)
    node3 = Node(3, None, None)
    node2 = Node(2, node3, None)
    node1 = Node(1, node2, node4)

    tree = Tree(node1)
    lca = find_lca(tree.root, 3, 5)
    print("LCA of 3, 5: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 2, 3)
    print("LCA of 2, 3: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 5, 4)
    print("LCA of 5, 4: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 2, 4)
    print("LCA of 2, 4: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 5, 1)
    print("LCA of 5, 1: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 6, 1)
    print("LCA of 6, 1: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 6, 7)
    print("LCA of 6, 7: %s" % (lca.data if lca else None))


if __name__ == '__main__':
    main()
