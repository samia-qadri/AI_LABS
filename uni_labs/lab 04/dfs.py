graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 4, 'E': 7},
    'C': {'A': 5, 'F': 3},
    'D': {'B': 4, 'G': 6},
    'E': {'B': 7, 'G': 1},
    'F': {'C': 3, 'G': 8},
    'G': {'D': 6, 'E': 1, 'F': 8}
}

MAX_STEPS = 30  # random search with no memory could go on forever, so we stop here

# ---------------------------------------------------------------
# 6. Depth First Search (uses a stack: last in, first out)
# ---------------------------------------------------------------
def depth_first_search(start, goal):
    stack = [[start]]        # stack of paths
    visited = []

    while stack != []:
        path = stack.pop()   # take from the TOP of the stack
        node = path[-1]

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            return visited, path

        # reversed so that alphabetical order is explored first
        neighbours = sorted(graph[node].keys())
        neighbours.reverse()
        for n in neighbours:
            if n not in visited:
                stack.append(path + [n])

    return visited, []