"""

Given a binary tree (not a binary search tree) and two values say n1 and n2, write a program to find the least common ancestor.
Following is definition of LCA from Wikipedia:
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in T that
has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).

The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from the root. Computation of
lowest common ancestors may be useful, for instance, as part of a procedure for determining the distance between pairs
of nodes in a tree: the distance from n1 to n2 can be computed as the distance from the root to n1, plus the distance
from the root to n2, minus twice the distance from the root to their lowest common ancestor.

Idea: The idea is to traverse the tree starting from root. If any of the given keys (n1 and n2) matches with root,
then root is LCA (assuming that both keys are present). If root doesnt match with any of the keys, we recur for left
and right subtree. The node which has one key present in its left subtree and the other key present in right subtree
is the LCA. If both keys lie in left subtree, then left subtree has LCA also, otherwise LCA lies in right subtree.
"""

from ds.trees.tree import Node
from ds.trees.tree import Tree


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
    node4 = Node(4, None, None)
    node3 = Node(3, node5, None)
    node2 = Node(2, None, node4)
    node1 = Node(1, node2, node3)

    tree = Tree(node1)
    lca = find_lca(tree.root, 4, 5)
    print("LCA of 4, 5: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 2, 3)
    print("LCA of 2, 3: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 2, 4)
    print("LCA of 2, 4: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 3, 5)
    print("LCA of 3, 5: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 5, 6)
    print("LCA of 5, 6: %s"%(lca.data if lca else None))

    lca = find_lca(tree.root, 6, 7)
    print("LCA of 6, 7: %s"%(lca.data if lca else None))


if __name__ == '__main__':
    main()


