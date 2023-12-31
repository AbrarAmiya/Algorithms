# -*- coding: utf-8 -*-
"""task1A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19f4CyBm9iu6_EFDPGByK4QfYVxMLwO3P
"""

def dfs_topological(node, graph, visited, result):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_topological(neighbor, graph, visited, result)
    result.insert(0, node)

def generate_topological_order(graph, n):
    parent_count = {node: 0 for node in range(1, n + 1)}

    for neighbors in graph.values():
        for neighbor in neighbors:
            parent_count[neighbor] += 1

    visited = [False] * (n + 1)
    result = []

    for node in range(1, n + 1):
        if not visited[node] and parent_count[node] == 0:
            dfs_topological(node, graph, visited, result)

    return result

def is_dag(graph):
    visited = set()
    stack = set()

    def dfs(node):
        visited.add(node)
        stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in stack:
                return True
        stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return False
    return True

def read_input(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().split())
        graph = {i: [] for i in range(1, n + 1)}
        for _ in range(m):
            a, b = map(int, file.readline().split())
            graph[a].append(b)
        return n, graph

def write_output(filename, result):
    with open(filename, 'w') as file:
        if result:
            file.write(" ".join(map(str, result)))
        else:
            file.write("IMPOSSIBLE\n")

# Driver code
if __name__ == "__main__":
    input_filename = "/content/input1A_1.txt"
    output_filename = "/content/output1A_1.txt"

    n, graph = read_input(input_filename)

    if is_dag(graph):
        result = generate_topological_order(graph, n)
        write_output(output_filename, result)

        print("Topological order:")
        print(result)
    else:
        write_output(output_filename, [])
        print("IMPOSSIBLE")