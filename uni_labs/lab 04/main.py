from random_searches import random_search
from random_searches import random_search_closed
from random_searches import random_search_open

from ucs import uniform_cost_search
from bfs import breadth_first_search
from dfs import depth_first_search

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


def print_graph():
    print("\nGraph (node: neighbour(cost)):")
    for node in graph:
        line = ""
        for neighbour in graph[node]:
            line = line + neighbour + "(" + str(graph[node][neighbour]) + ") "
        print("  " + node + ": " + line)


def get_path_cost(path):
    # add up the edge costs along the path
    total = 0
    for i in range(len(path) - 1):
        total = total + graph[path[i]][path[i + 1]]
    return total


def show_result(visited, path):
    print("\nNodes visited in order:", visited)
    if path == []:
        print("No path found.")
    else:
        print("Final path:", " -> ".join(path))
        print("Path cost:", get_path_cost(path))

# Menu and main program
# ---------------------------------------------------------------
def get_node(message):
    while True:
        node = input(message).strip().upper()
        if node in graph:
            return node
        print("Invalid node. Choose from:", list(graph.keys()))


def show_menu():
    print("\n========== SEARCH ALGORITHMS MENU ==========")
    print("1. Random Search")
    print("2. Random Search with Closed List")
    print("3. Random Search with Open List")
    print("4. Uniform Cost Search (UCS)")
    print("5. Breadth First Search (BFS)")
    print("6. Depth First Search (DFS)")
    print("7. Show graph")
    print("0. Exit")


def main():
    print_graph()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "7":
            print_graph()
            continue
        elif choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice, please try again.")
            continue

        start = get_node("Enter start node: ")
        goal = get_node("Enter goal node: ")

        if choice == "1":
            print("\n--- Random Search ---")
            visited, path = random_search(start, goal)
        elif choice == "2":
            print("\n--- Random Search with Closed List ---")
            visited, path = random_search_closed(start, goal)
        elif choice == "3":
            print("\n--- Random Search with Open List ---")
            visited, path = random_search_open(start, goal)
        elif choice == "4":
            print("\n--- Uniform Cost Search ---")
            visited, path = uniform_cost_search(start, goal)
        elif choice == "5":
            print("\n--- Breadth First Search ---")
            visited, path = breadth_first_search(start, goal)
        elif choice == "6":
            print("\n--- Depth First Search ---")
            visited, path = depth_first_search(start, goal)

        show_result(visited, path)


main()