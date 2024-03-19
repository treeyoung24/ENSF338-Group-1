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
        if node in self.adjacency_list:
            del self.adjacency_list[node]
            for adj_list in self.adjacency_list.values():
                adj_list[:] = [n for n in adj_list if n != node]

    def addEdge(self, n1, n2, weight=1):
        if n1 in self.adjacency_list and n2 in self.adjacency_list:
            self.adjacency_list[n1].append((n2, weight))
            self.adjacency_list[n2].append((n1, weight))

    def removeEdge(self, n1, n2):
        if n1 in self.adjacency_list and n2 in self.adjacency_list:
            self.adjacency_list[n1] = [(node, weight) for node, weight in self.adjacency_list[n1] if node != n2]
            self.adjacency_list[n2] = [(node, weight) for node, weight in self.adjacency_list[n2] if node != n1]

    def importFromFile(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                if not lines:
                    return None

                # Check if the graph is undirected
                if not lines[0].strip().startswith("strict graph"):
                    return None

                self.adjacency_list.clear()

                for line in lines[1:]:
                    line = line.strip()
                    if line and line[0] != '}':
                        if line[-1] == ';':
                            line = line[:-1]  # Remove trailing semicolon if present
                        parts = line.split('--')
                        if len(parts) != 2:
                            return None
                        node1 = parts[0].strip()
                        node2_weight = parts[1].strip().split('[')
                        node2 = node2_weight[0].strip()
                        weight = 1
                        if len(node2_weight) > 1:
                            weight_part = node2_weight[1].strip()[:-1]  # Remove closing bracket
                            weight_parts = weight_part.split('=')
                            if len(weight_parts) != 2 or weight_parts[0].strip() != 'weight':
                                return None
                            try:
                                weight = int(weight_parts[1].strip())
                            except ValueError:
                                return None

                        n1 = self.addNode(node1)
                        n2 = self.addNode(node2)
                        self.addEdge(n1, n2, weight)

                return self

        except FileNotFoundError:
            return None

        return None

# Example usage:
graph = Graph()
graph.importFromFile('example_graph.dot')
print(graph.adjacency_list)
