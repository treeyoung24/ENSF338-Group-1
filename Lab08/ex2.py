# 1. This queue could be implemented using linear search where nodes are appended to a list as they are discovered. To find the node with the smallest
# distance, a linear search is performed on the list. This would have a time complexity of O(n) for each operation. A faster implementation would be to
# use a priority queue where the priority of each node is determined by its distance from the source. To find the node with the smallest distance, the
# priority queue would return the node with the smallest priority. This would have a time complexity of O(log(n)) for each operation.

import heapq
import timeit

import matplotlib.pyplot as plt


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
        
    # 2.
    def slowSP(self, start_node):
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start_node] = 0
        visited = set()
        while len(visited) < len(self.adjacency_list):
            min_node = None
            min_distance = float('inf')
            for node, distance in distances.items():
                if node not in visited and distance < min_distance:
                    min_node = node
                    min_distance = distance
            if min_node is None:
                break
            visited.add(min_node)
            for neighbor, weight in self.adjacency_list[min_node]:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
        return distances

    def fastSP(self, start_node):
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.adjacency_list[current_node]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
        return distances

# 3.
def measure_performance(graph, algorithm_name):
    setup_code = f"from __main__ import graph"
    execution_code = f"graph.{algorithm_name}(list(graph.adjacency_list.keys())[0])"
    time_taken = timeit.timeit(execution_code, setup=setup_code, number=1)
    return time_taken

graph = Graph()
graph.importFromFile("C:\\ensf338\\ENSF338-Group-1\\Lab08\\random.dot")

slow_times = []
fast_times = []

for _ in range(5):  # Run each algorithm multiple times for better accuracy
    slow_time = measure_performance(graph, 'slowSP')
    fast_time = measure_performance(graph, 'fastSP')
    slow_times.append(slow_time)
    fast_times.append(fast_time)

slow_avg_time = sum(slow_times) / len(slow_times)
fast_avg_time = sum(fast_times) / len(fast_times)

slow_min_time = min(slow_times)
slow_max_time = max(slow_times)

fast_min_time = min(fast_times)
fast_max_time = max(fast_times)

print("Slow Algorithm:")
print("Average time:", slow_avg_time)
print("Min time:", slow_min_time)
print("Max time:", slow_max_time)

print("\nFast Algorithm:")
print("Average time:", fast_avg_time)
print("Min time:", fast_min_time)
print("Max time:", fast_max_time)

# 4.
plt.hist(slow_times, bins=10, alpha=0.5, label='Slow Algorithm')
plt.hist(fast_times, bins=10, alpha=0.5, label='Fast Algorithm')
plt.legend(loc='upper right')
plt.title('Distribution of Execution Times')
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.show()

# As expected, the histogram shows that the fast algorithm frequently has lower execution times than the slow algorithm. The fast algorithm uses a priority 
# queue to efficiently find the node with the smallest distance, resulting in a faster overall execution time compared to the slow algorithm, which uses linear
# search to find the node with the smallest distance. 