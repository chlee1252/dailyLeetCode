from collections import deque

def solution(maze, N, M):

   queue = deque([(0,0)])

   dx = [1, -1, 0, 0]
   dy = [0, 0, 1, -1]
   while queue:
      x, y = queue.popleft()

      for i in range(4):
         newX = x + dx[i]
         newY = y + dy[i]

         if newX > N-1 or newY > M-1 or newX < 0 or newY < 0 or maze[newX][newY] == 0:
            continue
         
         if maze[newX][newY] == 1:
            maze[newX][newY] = maze[x][y] + 1
            queue.append((newX, newY))
   
   return maze[N-1][M-1]


maze1 = [
   [1,0,1,0,1,0],
   [1,1,1,1,1,1],
   [0,0,0,0,0,1],
   [1,1,1,1,1,1],
   [1,1,1,1,1,1]
]

print(solution(maze1, 5, 6))


