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

    def _has_cycle(self, node, visited, path):
        visited.add(node)
        path.add(node)

        for neighbor, _ in self.adjacency_list[node]:  # Use the GraphNode object itself as the key
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

        for neighbor, _ in self.adjacency_list[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)

        stack.append(node)
        
# Example usage:
graph = Graph()
graph.importFromFile("D:\\Trevor School\\ENSF338\\ENSF338-Group-1\\Lab08\\random.dot")

if graph.isdag():
    print(graph.toposort())
else:
    print("The graph is not a DAG and cannot be sorted topologically.")
