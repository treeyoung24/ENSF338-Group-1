"""
Question 1
GitHub Copilot
A minimum spanning tree (MST) of a graph is a tree that spans all the vertices in the graph and has the minimum possible total edge weight. 
For example, consider a graph with 5 nodes and the following edges (represented as tuples of nodes and weights): (A-B, 1), (A-C, 3), (B-C, 4), 
(B-D, 2), (C-D, 5), (C-E, 6), (D-E, 7). The MST of this graph would be: (A-B, 1), (B-D, 2), (A-C, 3), (C-E, 6).
"""

#Question 2

class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def union(self, v1, v2):
        self.parent[self.find(v1)] = self.find(v2)

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def in_same_set(self, v1, v2):
        return self.find(v1) == self.find(v2)
    

# Question 3
    
    def mst(self):
    # Create a new graph for the MST
    mst = Graph()

    # Create a list of all edges sorted by weight
    edges = sorted(
        (weight, n1, n2) for n1, edges in self.adjacency_list.items() for n2, weight in edges
    )

    # Create a UNION-FIND structure for cycle detection
    union_find = UnionFind(self.adjacency_list.keys())

    # Add the smallest edges to the MST as long as they don't create a cycle
    for weight, n1, n2 in edges:
        if not union_find.in_same_set(n1, n2):
            mst.addEdge(n1, n2, weight)
            union_find.union(n1, n2)

    return mst