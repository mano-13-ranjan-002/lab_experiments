import heapq

# Greedy Best-First Search Algorithm
def greedy_best_first_search(start, goal, successors, heuristic):
    # Open list as a priority queue: (h, state, parent)
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start, None))

    # Keep track of parent pointers for reconstructing path
    parents = {}
    visited = set()

    while open_list:
        h, state, parent = heapq.heappop(open_list)

        # Skip if already visited
        if state in visited:
            continue
        visited.add(state)

        # Store parent
        parents[state] = parent

        # Goal test
        if state == goal:
            # Reconstruct path
            path = []
            node = state
            while node is not None:
                path.append(node)
                node = parents[node]
            return path[::-1]  # only path (no cost in GBFS)

        # Expand node
        for (child, cost) in successors(state):
            if child not in visited:
                heapq.heappush(open_list, (heuristic(child, goal), child, state))

    return None  # failure


# Example Graph
def successors(state):
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('C', 2), ('D', 5)],
        'B': [('D', 1)],
        'C': [('G', 5)],
        'D': [('G', 2)],
        'G': []
    }
    return graph.get(state, [])


# Heuristic Function
def heuristic(state, goal):
    h_values = {
        'S': 7,
        'A': 6,
        'B': 4,
        'C': 2,
        'D': 1,
        'G': 0
    }
    return h_values.get(state, 0)


# Run the Algorithm
if __name__ == "__main__":
    path = greedy_best_first_search('S', 'G', successors, heuristic)
    print("Path found:", path)
