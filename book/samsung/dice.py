n, m, i, j, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dice, tmp = [0] * 6, [0]*6
moves = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
direction = {1: (2, 0, 5, 3, 4, 1), 2: (1, 5, 0, 3, 4, 2), 3: (4, 1, 2, 0, 5, 3), 4: (3, 1, 2, 5, 0, 4)}

for command in commands:
    move = moves[command]
    ni, nj = i+move[0], j+move[1]
    if ni < 0 or nj < 0 or ni >= n or nj >= m:
        continue
    i, j = ni, nj
    for idx in range(6):
        tmp[idx] = dice[idx]
    dir = direction[command]
    for idx in range(6):
        dice[idx] = tmp[dir[idx]]
    
    if board[i][j]:
        dice[5] = board[i][j]
        board[i][j] = 0
    else:
        board[i][j] = dice[5]
    
    print(dice[0])

