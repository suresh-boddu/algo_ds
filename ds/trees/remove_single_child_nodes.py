from ds.trees.tree import Node
from ds.trees.tree import Tree


def remove_single_child_nodes(node):
    """
    Method to remove the nodes with single child (replace the current node with the single child so that its parent points to its single child)
    """

    if not node:
        return None

    if node.left and not node.right:
        return node.left
    elif node.right and not node.left:
        return node.right
    elif not (node.left or node.right):
        return node
    else:
        node.left = remove_single_child_nodes(node.left)
        node.right = remove_single_child_nodes(node.right)
        return node

def main():
    node5 = Node(5, None, None)
    node4 = Node(4, None, None)
    node3 = Node(3, node5, None)
    node2 = Node(2, None, node4)
    node1 = Node(1, node2, node3)

    tree = Tree(node1)

    print "Original Tree: \n"
    tree.in_order(tree.root)

    tree.root = remove_single_child_nodes(tree.root)

    print "Tree after removing the single child nodes: \n"
    tree.in_order(tree.root)

if __name__ == "__main__":
    main()