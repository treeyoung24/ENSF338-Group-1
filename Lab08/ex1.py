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
                if len(lines) < 3 or not lines[0].startswith("strict graph"):
                    return None
                
                for line in lines[2:]:
                    line = line.strip()
                    if line.endswith(";"):
                        line = line[:-1]
                    nodes = line.split("--")
                    if len(nodes) != 2:
                        return None
                    node1 = nodes[0].strip()
                    node2 = nodes[1].split("[")[0].strip()
                    weight = 1
                    if "weight" in line:
                        weight = int(line.split("[")[1].split("=")[1].split("]")[0].strip())
                    n1 = self.addNode(node1)
                    n2 = self.addNode(node2)
                    self.addEdge(n1, n2, weight)
        except FileNotFoundError:
            return None

# Example usage:
graph = Graph()
result = graph.importFromFile("example_graph.txt")
if result is not None:
    print(graph.adjacency_list)
else:
    print("Error: Unable to import graph from file.")
