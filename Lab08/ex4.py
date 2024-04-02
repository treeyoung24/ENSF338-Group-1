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

    def dfs(self):
        visited = set()
        result = []

        # Use the first node in the adjacency list as the starting node for DFS
        start_node = next(iter(self.adjacency_list.keys()))

        def dfs_util(node):
            visited.add(node)
            result.append(node.data)
            for neighbor, _ in self.adjacency_list[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start_node)
        return result

class Graph2(Graph):
    def __init__(self):
        super().__init__()
        self.adjacency_matrix = {}

    def addEdge(self, n1, n2, weight=None):
        super().addEdge(n1, n2, weight)
        if n1.data not in self.adjacency_matrix:
            self.adjacency_matrix[n1.data] = {}
        if n2.data not in self.adjacency_matrix:
            self.adjacency_matrix[n2.data] = {}
        self.adjacency_matrix[n1.data][n2.data] = weight
        self.adjacency_matrix[n2.data][n1.data] = weight

    def dfs(self):
        visited = set()
        result = []

        # Use the first node in the adjacency list as the starting node for DFS
        start_node = next(iter(self.adjacency_matrix.keys()))

        def dfs_util(node):
            visited.add(node)
            result.append(node)
            for neighbor in self.adjacency_matrix[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start_node)
        return result

# Define a function to measure the performance of dfs() for a given graph instance
def measure_dfs_performance(graph_instance, iterations=10):
    times = []
    for _ in range(iterations):
        start_time = time.time()
        graph_instance.dfs()
        end_time = time.time()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times

# Create instances of Graph and Graph2 classes
graph = Graph()
graph2 = Graph2()

# Import the graph from the file
result_graph = graph.importFromFile("C:\\ensf338\\ENSF338-Group-1\\Lab08\\random.dot")
result_graph2 = graph2.importFromFile("C:\\ensf338\\ENSF338-Group-1\\Lab08\\random.dot")

if result_graph and result_graph2:
    print("Graphs imported successfully.")
    # Measure performance of dfs() for Graph class
    graph_dfs_times = measure_dfs_performance(graph)
    print("Graph DFS performance:")
    print("Max time:", max(graph_dfs_times))
    print("Min time:", min(graph_dfs_times))
    print("Average time:", sum(graph_dfs_times) / len(graph_dfs_times))

    # Measure performance of dfs() for Graph2 class
    graph2_dfs_times = measure_dfs_performance(graph2)
    print("\nGraph2 DFS performance:")
    print("Max time:", max(graph2_dfs_times))
    print("Min time:", min(graph2_dfs_times))
    print("Average time:", sum(graph2_dfs_times) / len(graph2_dfs_times))
else:
    print("Failed to import graphs.")
