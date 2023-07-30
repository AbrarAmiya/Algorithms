# -*- coding: utf-8 -*-
"""task5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pVTqFYSUvU4hZr_38h1-QiKsP6mGX9ej
"""

def shortest_path(graph, start, end):
    queue = []
    queue.append(start)
    visited = set()
    visited.add(start)

    parent = {start: None}

    while queue:
        current_node = queue.pop(0)
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path
        for neighbor in graph[current_node]:
            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

                parent[neighbor] = current_node

    return None

with open('/content/input5.txt', 'r') as f:
    n, m, d = map(int, f.readline().split())
    graph = {i: [] for i in range(1, n+1)}

    for i in range(m):
        u, v = map(int, f.readline().split())
        graph[u].append(v)
        graph[v].append(u)


shortest_path_result = shortest_path(graph, 1, d)

with open('/content/output5.txt', 'w') as f:
    f.write('Time: ' + str(len(shortest_path_result) - 1) + '\n') # Writing the minimum amount of time to reach city D from city 1
    f.write('Shortest Path: ' + ' '.join(map(str, shortest_path_result))) # Writing the shortest path you will follow


print('Time:', len(shortest_path_result) - 1)
print('Shortest Path:', ' '.join(map(str, shortest_path_result)))