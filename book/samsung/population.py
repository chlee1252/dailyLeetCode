from collections import deque

n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
answer = 0 

moves = [(1,0), (-1,0), (0, 1), (0, -1)]
def allies(i,j):
    global is_move
    total, num = country[i][j], 1
    q = deque([(i, j)])
    visited = set()
    visited.add((i,j))

    while q:
        i,j = q.popleft()

        for move in moves:
            ni, nj = i+move[0], j+move[1]
            if ni < 0 or ni >= n or nj < 0 or nj >= n or (ni, nj) in visited:
                continue
            if l <= abs(country[i][j] - country[ni][nj]) <= r:
                is_move = True 
                total += country[ni][nj]
                num += 1
                visited.add((ni,nj))
                q.append((ni, nj))

    return total // num, visited
    
while True:
    total_visited = set()
    is_move = False
    union = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in total_visited:
                data, visited = allies(i, j)
                total_visited |= visited
                union.append((data, visited))

    for data, u in union:
        for c in u:
            x, y = c
            country[x][y] = data

    if not is_move:
        break
    answer += 1

print(answer)
