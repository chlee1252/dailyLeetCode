from collections import deque

n = int(input())
INF = float("inf")

graph = [[0]*n for _ in range(n)]
babyX, babyY = 0, 0
babyShark = 2

for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(n):
        if graph[i][j] == 9:
            babyX, babyY = i, j
            graph[i][j] = 0

moves = [(1,0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    dist = [[-1]*n for _ in range(n)]
    q = deque([(babyX, babyY)])
    dist[babyX][babyY] = 0
    while q:
        x, y = q.popleft()

        for move in moves:
            nx, ny = move[0]+x, move[1]+y

            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] > babyShark:
                continue
            
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < babyShark:
                if min_dist > dist[i][j]:
                    x, y = i, j
                    min_dist = dist[i][j]
    
    if min_dist == INF:
        return -1
    
    return x, y, min_dist

result = 0
ate = 0
while True:
    value = find(bfs())

    if value == -1:
        print(result)
        break
    
    babyX, babyY = value[0], value[1]
    result += value[2]

    graph[babyX][babyY] = 0
    ate += 1

    if ate >= babyShark:
        babyShark += 1
        ate = 0

