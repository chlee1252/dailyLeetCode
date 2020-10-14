n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

tetrominoes = [
    [(0,0), (0,1), (1,0), (1,1)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (0,1), (1,1), (2,1)],
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

result = float('-inf')
for i in range(n):
    for j in range(m):
        for tetromino in tetrominoes:
            tmp = 0
            for tet in tetromino:
                x, y = tet
                # Python3 성공
                # try:
                #     nx = i+x
                #     ny = j+y
                #     tmp += board[nx][ny]
                # except IndexError:
                #     continue
                
                # Pypy3 성공
                nx, ny = i+tet[0], j+tet[1]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                tmp += board[nx][ny]
            result = max(result, tmp)

print(result)

