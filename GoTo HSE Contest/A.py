import sys
import math

graph = {
    -1: [7, 0],
    0: [-1, 10, 8],
    1: [2, 4],
    2: [1, 5, 3],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8, -1],
    8: [5, 7, 0, 9],
    9: [6, 8, 10],
    10: [0, 9]
}


def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            visited.add(vertex)


def rasst(a, b):
    x = bfs(graph, a, b)
    if x:
        return len(bfs(graph, a, b)) - 1
    else:
        return 0


sys.stdin = open("input.txt")
s = input()

cur = -1
res = 0
for num in s:
    S = rasst(cur, int(num))
    res += S
    res += 1
    cur = int(num)

S = rasst(cur, 10)
res += S
res += 1

print(res)
