from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

moves = [(0,1), (0,-1), (-1,0), (1,0)]
q = deque([(0,0,1)])
maze[0][0] = 0
while q:
    x,y,step = q.popleft()
    if x == N-1 and y == M-1:
        print(step)
        break
            
    for move in moves:
        i, j = move
        newX, newY = x+i, y+j
        if newX < 0 or newX > N-1 or newY < 0 or newY > M-1 or maze[newX][newY] == 0:
            continue
        maze[newX][newY] = 0
        q.append((x+i, y+j, step+1))



# def solution(N, M, maze):

#     moves = [(0,1), (0,-1), (-1,0), (1,0)]
#     q = deque([(0,0,1)])
#     maze[0][0] = 0
#     while q:
#         x,y,step = q.popleft()
#         if x == N-1 and y == M-1:
#             return step
            
#         for move in moves:
#             i, j = move
#             newX, newY = x+i, y+j
#             if newX < 0 or newX > N-1 or newY < 0 or newY > M-1 or maze[newX][newY] == 0:
#                 continue
#             q.append((x+i, y+j, step+1))

#     return -1            

# maze1 = [[1,0,1,0,1,0], [1,1,1,1,1,1], [0,0,0,0,0,1], [1,1,1,1,1,1], [1,1,1,1,1,1]]
# maze2 = [[1,1,0],[0,1,0],[0,1,1]]
# print(solution(5, 6, maze1))
# print(solution(3,3,maze2))

