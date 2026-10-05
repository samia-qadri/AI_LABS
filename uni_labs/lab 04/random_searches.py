import random

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
# 1. Random Search (no memory at all)
# ---------------------------------------------------------------
def random_search(start, goal):
    current = start
    visited = [current]
    path = [current]
    steps = 0

    while current != goal and steps < MAX_STEPS:
        neighbours = list(graph[current].keys())
        current = random.choice(neighbours)   # pick any neighbour randomly
        visited.append(current)
        path.append(current)
        steps = steps + 1

    if current != goal:
        print("\nGoal not found in", MAX_STEPS, "steps (it kept wandering).")
        return visited, []
    return visited, path

# ---------------------------------------------------------------
# 2. Random Search with Closed List
# ---------------------------------------------------------------
def random_search_closed(start, goal):
    closed = []          # nodes we already visited
    current = start
    path = []

    while True:
        closed.append(current)
        path.append(current)

        if current == goal:
            return closed, path

        # only choose neighbours that are NOT in the closed list
        choices = []
        for n in graph[current]:
            if n not in closed:
                choices.append(n)

        if choices == []:
            print("\nStuck! Every neighbour was already visited (dead end).")
            return closed, []

        current = random.choice(choices)


# ---------------------------------------------------------------
# 3. Random Search with Open List
# ---------------------------------------------------------------
def random_search_open(start, goal):
    open_list = [start]      # nodes found but not explored yet
    closed = []              # nodes already explored
    parent = {start: None}   # remembers how we reached each node

    while open_list != []:
        current = random.choice(open_list)   # pick a RANDOM node from open list
        open_list.remove(current)
        closed.append(current)

        if current == goal:
            # build the path by going back through the parents
            path = []
            node = goal
            while node is not None:
                path.insert(0, node)
                node = parent[node]
            return closed, path

        for n in graph[current]:
            if n not in closed and n not in open_list:
                open_list.append(n)
                parent[n] = current

    return closed, []