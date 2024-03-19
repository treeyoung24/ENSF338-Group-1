import heapq

class Graph:

    def slowSP(self, node):
        distances = {node: 0}
        visited = set()
        while len(visited) < len(self.adjacency_list):
            min_node = None
            min_distance = float('inf')
            for n in self.adjacency_list:
                if n not in visited and n in distances and distances[n] < min_distance:
                    min_node = n
                    min_distance = distances[n]
            if min_node is None:
                break
            visited.add(min_node)
            for neighbor, weight in self.adjacency_list[min_node]:
                if neighbor not in distances or distances[min_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[min_node] + weight
        return distances

    def fastSP(self, node):
        distances = {node: 0}
        visited = set()
        queue = [(0, node)]
        while queue:
            min_distance, min_node = heapq.heappop(queue)
            if min_node in visited:
                continue
            visited.add(min_node)
            for neighbor, weight in self.adjacency_list[min_node]:
                if neighbor not in distances or min_distance + weight < distances[neighbor]:
                    distances[neighbor] = min_distance + weight
                    heapq.heappush(queue, (distances[neighbor], neighbor))
        return distances
