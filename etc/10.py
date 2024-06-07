# 인접 행렬을 사용한 그래프 표현
# A, B, C, D를 각각 0, 1, 2, 3으로 매핑
graph = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0]   # D
]

# 그래프 출력
for row in graph:
    print(row)

# 인접 리스트를 사용한 그래프 표현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# 그래프 출력
for vertex in graph:
    print(f'{vertex}: {graph[vertex]}')

def dfs(graph, start):
    visited = set()
    stack = [start]
    print(stack)

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in (graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H', 'I'],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

dfs(graph, 'A')
# 출력: A C G F B E I H D

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H', 'I'],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

bfs(graph, 'A')
# 출력: A B C D E F G H I