import heapq
from collections import defaultdict

def ucs(graph, start, goal):
    # Priority queue: elements are tuples (cost, node, path)
    frontier = []
    heapq.heappush(frontier, (0, start, [start]))

    explored = set()

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        if node == goal:
            return cost, path

        if node not in explored:
            explored.add(node)

            for neighbor, edge_cost in graph[node]:
                if neighbor not in explored:
                    heapq.heappush(frontier, (cost + edge_cost, neighbor, path + [neighbor]))

    return float("inf"), []  # Goal not reachable

# Example usage:
# Graph represented as adjacency list with costs: node -> list of (neighbor, cost)
graph = defaultdict(list)
graph['A'] = [('B', 1), ('C', 4)]
graph['B'] = [('C', 2), ('D', 5)]
graph['C'] = [('D', 1)]
graph['D'] = []

start_node = 'A'
goal_node = 'D'

cost, path = ucs(graph, start_node, goal_node)
print(f"Minimum cost from {start_node} to {goal_node}: {cost}")
print(f"Path: {' -> '.join(path)}")
