from collections import deque
import sys

input = sys.stdin.readline
moves = [(1,0), (-1,0), (0, 1), (0,-1)]
DEL = "DEL"

n, m, t = map(int, input().split())
q = [deque([0]) for _ in range(n+1)]
for i in range(1, n+1):
    numbers = list(map(int, input().split()))
    for n in numbers:
        q[i].append(n)

# print(q[4])

def solve(i, j):
    queue = deque([(i, j)])
    visited = [[False] * (m+1) for _ in range(n+1)]
    visited[i][j] = True
    adj = False

    while queue:
        x, y = queue.popleft()

        for move in moves:
            nx, ny = move[0]+x, move[1]+y
            if nx < 1 or ny < 1 or nx > n or ny > m or visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            if q[x][y] == q[nx][ny]:
                q[x][y] = DEL
                q[nx][ny] = DEL
                adj = True
            else:
                queue.append((nx, ny))
    print(q)
    if not adj:
        average = 0
        total = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if q[i][j] != DEL:
                    average += q[i][j]
                    total += 1
        
    else:
        result = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if q[i][j] != DEL:
                    result += q[i][j]
        
        print(result)

for _ in range(t):
    x, d, k = map(int, input().split())
    for i in range(1, len(q)):
        if i % x == 0:
            k = k if d == 0 else -k
            q[i].rotate(k)
    solve(1,1)



# for _ in range(t):
#     x, d, k = map(int, input().split())

#     for i in range(1, len(q)+1):
#         if i % x == 0:
#             k = k if d == 0 else -k
#             q[i-1] = q[i-1].rotate(k)
    
#     print(q)