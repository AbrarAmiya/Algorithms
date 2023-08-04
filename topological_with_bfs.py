# -*- coding: utf-8 -*-
"""Task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tdSxL4XyJq0JS5DAwgjp4eoPJOtgcARO
"""

def bfs(graph, start_node):
    visited = []  # To keep track of visited nodes
    queue = [start_node]  # Initialize the queue with the starting node
    visited.append(start_node)  # Mark the starting node as visited

    while queue:
        current_node = queue.pop(0)  # Dequeue the front node

        # Process the current node (print or store it as needed)
        print(current_node, end=" ")  # Printing the current node

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Enqueue the neighbor for further exploration

# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

start_node = 1
print("BFS traversal:")
bfs(graph, start_node)
print()
print(graph[1])

def bfs_recursive(graph, queue):
    if not queue:
        return

    current_node = queue.pop(0)
    print(current_node, end=" ")

    for neighbor in graph[current_node]:
        if neighbor not in queue:
            queue.append(neighbor)

    bfs_recursive(graph, queue)

# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5,6],
    4: [6],
    5: [],
    6: [],
    7: [4]
}

start_node = 1
print("BFS traversal:")
bfs_recursive(graph, [start_node])

def bfs_recursive(graph, queue, visited):
    if not queue:
        return

    current_node = queue.pop(0)
    if current_node not in visited:
        print(current_node, end=" ")
        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    bfs_recursive(graph, queue, visited)

# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5, 6],
    4: [6],
    5: [],
    6: [7],
    7: [4]
}

start_node = 1
print("BFS traversal:")
bfs_recursive(graph, [start_node], set())

def topological_sort(graph, node, visited, stack):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            topological_sort(graph, neighbor, visited, stack)

    stack.insert(0, node)

def bfs_topological(graph):
    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            topological_sort(graph, node, visited, stack)

    return stack

# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5, 6],
    4: [6],
    5: [],
    6: [7],
    7: [4]
}

graph_1 = {
    1: [2],
    2: [],  # Corrected missing comma here
    3: [1],
    4: [5],
    5: []
}

print("Topological order:")
result = bfs_topological(graph)
print(result)

print("Topological order:")
result1 = bfs_topological(graph_1)
print(result1)

from collections import defaultdict, deque

def topological_sort(graph):
    indegree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque()
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    topological_order = []
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topological_order

# Example graph represented as an adjacency list
graph = {
    1: [2],
    2: [],
    3: [1],
    4: [5],
    5: []
}

print("Topological order:")
result = topological_sort(graph)
print(result)

def bfs_topological(graph):
    indegree = {}  # Keep track of the indegree of each node
    for node in graph:
        indegree[node] = 0

    # Calculate the indegree of each node
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = []
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    topological_order = []
    while queue:
        node = queue.pop(0)
        topological_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topological_order

# Example graph represented as an adjacency list
graph = {
    1: [2],
    2: [],
    3: [1],
    4: [5],
    5: []
}

print("Topological order:")
result = bfs_topological(graph)
print(result)