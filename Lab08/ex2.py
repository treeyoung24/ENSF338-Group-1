# 1. This queue could be implemented using linear search where nodes are appended to a list as they are discovered. To find the node with the smallest
# distance, a linear search is performed on the list. This would have a time complexity of O(n) for each operation. A faster implementation would be to
# use a priority queue where the priority of each node is determined by its distance from the source. To find the node with the smallest distance, the
# priority queue would return the node with the smallest priority. This would have a time complexity of O(log(n)) for each operation.

import random
import sys
import timeit


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

    def slowSP(self, source):
        distances = {node: sys.maxsize for node in self.adjacency_list}
        distances[source] = 0
        unvisited = set(self.adjacency_list.keys())

        while unvisited:
            min_node = None
            min_distance = sys.maxsize
            for node in unvisited:
                if distances[node] < min_distance:
                    min_distance = distances[node]
                    min_node = node

            unvisited.remove(min_node)

            for neighbor, weight in self.adjacency_list[min_node]:
                if distances[min_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[min_node] + weight

        return distances

    def fastSP(self, source):
        distances = {node: sys.maxsize for node in self.adjacency_list}
        distances[source] = 0
        unvisited = set(self.adjacency_list.keys())

        while unvisited:
            min_node = min(unvisited, key=lambda x: distances[x])
            unvisited.remove(min_node)

            for neighbor, weight in self.adjacency_list[min_node]:
                if distances[min_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[min_node] + weight

        return distances

# Function to measure time taken by an algorithm
def measure_time(algorithm_func, graph):
    return timeit.timeit(lambda: algorithm_func(random.choice(list(graph.adjacency_list.keys()))), number=1)

# Define the number of iterations for averaging
num_iterations = 10
slow_times = []
fast_times = []

graph = Graph()
if graph.importFromFile("random.dot") is None:
    print("Error: Failed to load the graph from file")
else:
    # Measure time for slowSP
    for _ in range(num_iterations):
        slow_time = measure_time(graph.slowSP, graph)
        slow_times.append(slow_time)

    # Measure time for fastSP
    for _ in range(num_iterations):
        fast_time = measure_time(graph.fastSP, graph)
        fast_times.append(fast_time)

    # Calculate averages, max, and min
    avg_slow_time = sum(slow_times) / num_iterations
    max_slow_time = max(slow_times)
    min_slow_time = min(slow_times)

    avg_fast_time = sum(fast_times) / num_iterations
    max_fast_time = max(fast_times)
    min_fast_time = min(fast_times)

    # Print results
    print("Slow Version:")
    print(f"Average time: {avg_slow_time}")
    print(f"Max time: {max_slow_time}")
    print(f"Min time: {min_slow_time}")

    print("\nFast Version:")
    print(f"Average time: {avg_fast_time}")
    print(f"Max time: {max_fast_time}")
    print(f"Min time: {min_fast_time}")
