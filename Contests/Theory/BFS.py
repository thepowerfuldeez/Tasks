from collections import deque


def BFS(start, finish, graph, V):
    dist = [None] * V
    a = deque()
    a.append(start - 1)

    while a:
        v = a.pop()
        for u in graph[v]:
            if dist[u] is not None:
                dist[u] = dist[v] + 1
                a.append(u)
    return dist

