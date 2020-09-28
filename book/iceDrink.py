def dfs(x, y, xMax, yMax, tray):
   if x > xMax-1 or y > yMax-1 or x < 0 or y < 0 or tray[x][y] == 1:
      return False
   
   tray[x][y] = 1
   
   dfs(x+1, y, xMax, yMax, tray)
   dfs(x-1, y, xMax, yMax, tray)
   dfs(x, y+1, xMax, yMax, tray)
   dfs(x, y-1, xMax, yMax, tray)

   return True

def solution(tray):
   result = 0
   N, M = len(tray), len(tray[0])
   for i in range(N):
      for j in range(M):
         if tray[i][j] == 0:
            if dfs(i, j, N, M, tray):
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
print(solution(tray1))
print(solution(tray2))

assert solution(tray1) == 3
assert solution(tray2) == 8
   



      