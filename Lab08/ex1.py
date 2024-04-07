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

# Create an instance of the Graph class
graph = Graph()

# Call importFromFile method with the path to the GraphViz file
result = graph.importFromFile("random.dot") # Change the file path as needed

# Check the result of the import operation
if result:
    print("Graph imported successfully.")
else:
    print("Failed to import graph.")
