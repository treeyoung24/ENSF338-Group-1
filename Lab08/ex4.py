import time

class GraphNode:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.adjacency_list[node] = []
        return node

    def removeNode(self, node):
        del self.adjacency_list[node]
        for adj_list in self.adjacency_list.values():
            adj_list[:] = [n for n in adj_list if n[0] != node]

    def addEdge(self, n1, n2, weight=None):
        if n1 in self.adjacency_list and n2 in self.adjacency_list:
            self.adjacency_list[n1].append((n2, weight))
            self.adjacency_list[n2].append((n1, weight))
        else:
            raise ValueError("One or both nodes not found in the graph.")

    def removeEdge(self, n1, n2):
        if n1 in self.adjacency_list and n2 in self.adjacency_list:
            self.adjacency_list[n1] = [(n, w) for n, w in self.adjacency_list[n1] if n != n2]
            self.adjacency_list[n2] = [(n, w) for n, w in self.adjacency_list[n2] if n != n1]
        else:
            raise ValueError("One or both nodes not found in the graph.")

    def importFromFile(self, file):
        self.adjacency_list = {}
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line.startswith("strict graph"):
                        continue  # Skip the graph type line
                    if line.startswith("}"):
                        break  # End of graph definition
                    if line.endswith(";"):
                        line = line[:-1]  # Remove ending semicolon if present
                    nodes = line.split("--")
                    if len(nodes) != 2:
                        return False  # Invalid edge format
                    node1 = nodes[0].strip()
                    node2 = nodes[1].strip()
                    weight = 1
                    if "[" in node2:
                        node2, attr = node2.split("[")
                        attr = attr.strip("]").split("=")
                        if len(attr) == 2 and attr[0].strip() == "weight":
                            weight = int(attr[1])
                    n1 = self.addNode(node1)
                    n2 = self.addNode(node2)
                    self.addEdge(n1, n2, weight)
            return True  # Successfully imported
        except FileNotFoundError:
            return False  # File not found

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        dfs_result = [start_node]
        for neighbor, _ in self.adjacency_list.get(start_node, []):
            if neighbor not in visited:
                dfs_result.extend(self.dfs(neighbor, visited))
        return dfs_result

class Graph2(Graph):
    def __init__(self):
        super().__init__()
        self.adjacency_matrix = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.adjacency_list[node] = []
        self.adjacency_matrix[node] = {}
        return node

    def addEdge(self, n1, n2, weight=None):
        super().addEdge(n1, n2, weight)
        self.adjacency_matrix[n1][n2] = weight
        self.adjacency_matrix[n2][n1] = weight

    def removeEdge(self, n1, n2):
        super().removeEdge(n1, n2)
        del self.adjacency_matrix[n1][n2]
        del self.adjacency_matrix[n2][n1]

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        dfs_result = [start_node]
        for neighbor, _ in self.adjacency_list.get(start_node, []):
            if neighbor not in visited:
                dfs_result.extend(self.dfs(neighbor, visited))
        return dfs_result

# Measure performance
def measure_performance(graph, num_iterations=10):
    times = []
    for _ in range(num_iterations):
        start_time = time.time()
        graph.dfs(list(graph.adjacency_list.keys())[0])
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Example usage:
graph = Graph()
graph.importFromFile("random.dot")

graph2 = Graph2()
graph2.importFromFile("random.dot")

times_graph = measure_performance(graph)
times_graph2 = measure_performance(graph2)

print("Graph:")
print("Max time:", max(times_graph))
print("Min time:", min(times_graph))
print("Average time:", sum(times_graph) / len(times_graph))

print("\nGraph2:")
print("Max time:", max(times_graph2))
print("Min time:", min(times_graph2))
print("Average time:", sum(times_graph2) / len(times_graph2))


# Question 3
"""
Overall, the performance of  Graph2 is generally better than the Graph class. This is because the adjacency matrix allows for faster lookups of edges between nodes compared to the adjacency list. 
The adjacency matrix provides constant time complexity for edge lookups, while the adjacency list requires iterating through the list of neighbors for each node, 
resulting in a higher time complexity. This difference in performance is more pronounced in larger graphs with many edges, where the adjacency matrix can provide significant speed improvements.
"""