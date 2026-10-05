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
# 4. Uniform Cost Search (always expand the cheapest path so far)
# ---------------------------------------------------------------
def uniform_cost_search(start, goal):
    open_list = [[0, start, [start]]]   # each item: [cost so far, node, path]
    closed = []
    visited = []

    while open_list != []:
        # find the item with the lowest cost
        best = open_list[0]
        for item in open_list:
            if item[0] < best[0]:
                best = item
        open_list.remove(best)

        cost = best[0]
        node = best[1]
        path = best[2]

        if node in closed:
            continue
        closed.append(node)
        visited.append(node)

        if node == goal:
            return visited, path

        for n in graph[node]:
            if n not in closed:
                new_cost = cost + graph[node][n]
                open_list.append([new_cost, n, path + [n]])

    return visited, []