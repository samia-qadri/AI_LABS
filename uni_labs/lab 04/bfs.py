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
# 5. Breadth First Search (uses a queue: first in, first out)
# ---------------------------------------------------------------
def breadth_first_search(start, goal):
    queue = [[start]]        # queue of paths
    visited = [start]
    explored = []

    while queue != []:
        path = queue.pop(0)  # take from the FRONT of the queue
        node = path[-1]
        explored.append(node)

        if node == goal:
            return explored, path

        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                queue.append(path + [n])   # add to the BACK of the queue

    return explored, []
