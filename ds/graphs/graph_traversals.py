from ds.graphs.graph import Graph
from ds.graphs.graph import Node


def main():
    node5 = Node(5)
    node4 = Node(4)
    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1)

    node1.neighbours = [node2, node3]
    node2.neighbours = [node1, node4]
    node3.neighbours = [node1, node5]
    node4.neighbours = [node2, node5]
    node5.neighbours = [node3, node4]

    graph = Graph(node1)

    print "BFS: \n"
    graph.bfs(graph.root)

    print "Recursive DFS: \n"
    graph.recursive_dfs(graph.root)

    print "Iterative DFS: \n"
    graph.iterative_dfs(graph.root)


if __name__ == "__main__":
    main()