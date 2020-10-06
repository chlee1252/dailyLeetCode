from collections import deque

n = int(input().split()[0])
graph = [list(map(int, input().split())) for _ in range(n)]
data = [(graph[i][j], 0, i, j) for j in range(n) for i in range(n) if graph[i][j] != 0]
s, x, y = map(int, input().split())
moves = [(1,0), (-1,0), (0,1), (0,-1)]

data.sort()
q = deque(data)

while q:
    virus, sec, i, j = q.popleft()
    if sec == s:
        break

    for move in moves:
        nx, ny = i+move[0], j+move[1]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, sec+1, nx, ny))
print(graph[x-1][y-1])



# visited = [[False] * n for _ in range(n)]


# moves = [(1,0), (-1,0), (0,1), (0,-1)]
# def spread(i, j, virus):
#     for move in moves:
#         nx, ny = i+move[0], j+move[1]
#         if nx >= 0 and ny >= 0 and nx < n and ny < n:
#             if graph[nx][ny] == 0:
#                 visited[nx][ny] = True
#                 graph[nx][ny] = virus

# while s > 0:
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] != 0 and not visited[i][j]:
#                 visited[i][j] = True
#                 spread(i, j, graph[i][j])
    
#     visited = [[False] * n for _ in range(n)]
#     s -= 1

# print(graph[x-1][y-1])
