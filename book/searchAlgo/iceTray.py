def dfs(graph, i, j, xMax, yMax):
    if i > xMax-1 or i < 0 or j > yMax-1 or j < 0 or graph[i][j] == 1:
        return False
    
    graph[i][j] = 1
    
    dfs(graph, i+1, j, xMax, yMax)
    dfs(graph, i-1, j, xMax, yMax)
    dfs(graph, i, j-1, xMax, yMax)
    dfs(graph, i, j+1, xMax, yMax)

    return True

def solution(N, M, tray):
    result = 0
    for i in range(N):
        for j in range(M):
            if tray[i][j] == 0:
                dfs(tray, i, j, N, M)
                result += 1
    
    return result
tray1 = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
tray2 = [
   [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
   [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
   [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
   [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
   [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
   [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
   [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
   [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
   [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
   [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
   [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
   [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
   [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
   [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
]

print(solution(4,5, tray1))
print(solution(15,14, tray2))