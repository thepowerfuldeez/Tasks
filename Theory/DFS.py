WHITE = 0  # Не побывали в вершине
BLACK = 1  # Побывали
V = 7  # количество вершин
color = [0] * V

graph = [[1], [0, 2], [1, 3, 4, 5], [2], [2, 6], [2], [4]]


def dfs(v):
    """Рекурсивный алгоритм обхода всех вершин ациклического графа"""

    color[v] = BLACK
    for u in graph[v]:
        if color[u] == WHITE:
            print("Я в {}-й позиции.".format(u + 1))
            dfs(u)

dfs(0)