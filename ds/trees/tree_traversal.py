from ds.trees.tree import Node
from ds.trees.tree import Tree


def main():
    node5 = Node(5, None, None)
    node4 = Node(4, None, None)
    node3 = Node(3, node5, None)
    node2 = Node(2, None, node4)
    node1 = Node(1, node2, node3)

    tree = Tree(node1)

    print "InOrder: \n"
    tree.in_order(tree.root)

    print "PreOrder: \n"
    tree.pre_order(tree.root)

    print "PostOrder: \n"
    tree.post_order(tree.root)

    print "LevelOrder: \n"
    tree.level_order(tree.root)


if __name__ == "__main__":
    main()