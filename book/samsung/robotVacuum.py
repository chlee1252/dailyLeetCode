n, m = map(int, input().split())
i, j, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
direc = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
answer = 1
room[i][j] = 2

# 0이 벽, 1이 빈칸, 2가 청소한거
while True:
    # 네방향 모두 탐색
    checked =  False
    for _ in range(4):
        d = (d+3) % 4
        ni, nj = i+direc[d][0], j+direc[d][1]

        if not room[ni][nj]:
            room[ni][nj] = 2
            i, j = ni, nj
            checked = True
            answer += 1
            break
    
    if not checked:
        if room[i-direc[d][0]][j-direc[d][1]] == 1:
            break
        else:
            i, j = i-direc[d][0], j-direc[d][1]

print(answer)
                

            
        
        

