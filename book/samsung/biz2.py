from collections import deque

n, m = map(int, input().split())
maps = [[] for _ in range(n)]
r, b = None, None

for i in range(n):
    maps[i] = list(input())
    for j in range(m):
        if maps[i][j] == 'R':
            r = (i, j)
        elif maps[i][j] == 'B':
            b = (i, j)
direction = [(1,0), (-1,0), (0, 1), (0, -1)]

def move(i, j, di, dj):
    c = 0
    while maps[i+di][j+dj] != '#' and maps[i][j] != 'O':
        i, j = i+di, j+dj
        c += 1
    
    return i, j, c

def bfs(r1, r2, b1, b2, c):
    q = deque([(r1, r2, b1, b2, c)])
    visited = set((r1, r2, b1, b2))

    while q:
        ri, rj, bi, bj, c = q.popleft()

        if c > 10:
            return -1
        
        for di, dj in direction:
            rni, rnj, rc = move(ri, rj, di, dj)
            bni, bnj, bc = move(bi, bj, di, dj)

            if maps[bni][bnj] != 'O':
                if maps[rni][rnj] == 'O':
                    return c
                
                if rni == bni and rnj == bnj:
                    if rc > bc:
                        rni, rnj = rni-di, rnj-dj
                    else:
                        bni, bnj = bni - di, bnj - dj
                
                if (rni, rnj, bni, bnj) not in visited:
                    visited.add((rni, rnj, bni, bnj))
                    q.append((rni, rnj, bni, bnj, c+1))
    
    return -1


print(bfs(r[0], r[1], b[0], b[1], 1))
        


