n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

tmp = [[0] * m for _ in range(n)]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0

def virus(i, j):
    for move in moves:
        nx, ny = move[0]+i, move[1]+j
        if nx >= 0 and ny >= 0 and nx < n and ny < m:    
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)

def safeArea():
    safe = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                safe += 1
    return safe

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]
        
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
      
        result = max(result, safeArea())
        return
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    count += 1
                    dfs(count)
                    graph[i][j] = 0
                    count -= 1

dfs(0)
print(result)
