# 1. Topological sorting can be implemented using an algorithm seen in class. Which algorithm? Why?
    
# Topological sorting can be implemented using DFS algorithm. We use this algorithm because DFS visits each vertex in the graph and keeps the finish times and discovery of each vertex. Printing vertex after its recursive calls will give us the topological sorting.

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
                    if len(nodes) == 2:  # Ensure there are two nodes
                        node1, node2 = nodes[0], nodes[1]
                        if node1 not in self.adjacency_list:
                            self.adjacency_list[node1] = []
                        if node2 not in self.adjacency_list:
                            self.adjacency_list[node2] = []
                        # Add edge between node1 and node2
                        self.adjacency_list[node1].append((node2, 1))  # Assuming weight is 1
                        self.adjacency_list[node2].append((node1, 1))  # Assuming weight is 1
        except FileNotFoundError:
            print(f"File {file} not found.")
            return None

    def _has_cycle(self, node, visited, path):
        visited.add(node)
        path.add(node)

        for neighbor in self.adjacency_list[node]:
            if neighbor not in visited:
                if self._has_cycle(neighbor, visited, path):
                    return True
            elif neighbor in path:
                return True

        path.remove(node)
        return False

    def isdag(self):
        visited = set()
        path = set()

        for node in self.adjacency_list:
            if node not in visited:
                if self._has_cycle(node, visited, path):
                    return False
        return True
    
    def toposort(self):
        if not self.isdag():
            return None

        visited = set()
        stack = []

        for node in self.adjacency_list:
            if node not in visited:
                self._dfs(node, visited, stack)

        return stack[::-1]
    
    def _dfs(self, node, visited, stack):
        visited.add(node)

        for neighbor in self.adjacency_list[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)

        stack.append(node)

# Example usage:
graph = Graph()
result = graph.importFromFile("D:\\Trevor School\\ENSF338\\ENSF338-Group-1\\Lab08\\random.dot")
if result is not None:
    print(graph.adjacency_list)
else:
    print("Error: Unable to import graph from file.")

