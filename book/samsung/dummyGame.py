from collections import deque

n = int(input())
apple = 'apple'
apple_count = int(input())
answer = 0

board = [[0] * n for _ in range(n)]

for _ in range(apple_count):
    i, j = map(int, input().split())
    board[i-1][j-1] = apple

direc_count = int(input())
direc = deque([])
tail = [0,0]

move = {1: (0,1), 2: (-1,0), 3: (0,-1), 4:(1,0)}
cur_move = 1

# 뱀=1 사과='apple' 빈공간=0
for _ in range(direc_count):
    sec, d = input().split()
    direc.append((int(sec), d))

snake = deque([(0,0)])

i, j = 0, 0
while True:
    if direc and answer == direc[0][0]:
        new_direc = direc.popleft()
        if new_direc[1] == 'L':
            if cur_move + 1 == 5:
                cur_move = 1
            else:
                cur_move += 1
        elif new_direc[1] == 'D':
            if cur_move - 1 == 0:
                cur_move = 4
            else:
                cur_move -= 1
    
    # 방향에 따라서 좌표 계산
    ni, nj = move[cur_move][0]+i, move[cur_move][1]+j
    if ni < 0 or nj < 0 or ni >= n or nj >= n or board[ni][nj] == 1:
        answer += 1
        break
    
    # 뱀에 추가
    snake.append((ni, nj))
    i, j = ni, nj
    
    if board[ni][nj] != apple:
        # 꼬리 좌표 팝
        ti, tj = snake.popleft()
        # 꼬리 좌표 0으로 변환
        board[ti][tj] = 0

    board[ni][nj] = 1
    answer += 1
    

print(answer)
