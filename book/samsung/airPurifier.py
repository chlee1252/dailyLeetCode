r, c, t = map(int, input().split())
room = []
purifier = []

for _ in range(r): 
    room.append(list(map(int, input().split())))

now = (0, 0)
for i in range(r):
    if room[i][0] == -1 and room[i+1][0] == -1:
        now = (i, i+1)
        break

def circulate(room):
    temp = room[now[0]][c-1]
    for i in range(c-2, 0, -1):
        room[now[0]][i+1] = room[now[0]][i]
    
    temp2 = room[0][c-1]
    for i in range(now[0]-1):
        room[i][c-1] = room[i+1][c-1]
    room[now[0]-1][c-1] = temp

    temp = room[0][0]
    for i in range(c-1):
        room[0][i] = room[0][i+1]
    room[0][c-2] = temp2

    for i in range(now[0]-1, 1, -1):
        room[i][0] = room[i-1][0]
    room[now[0]][1] = 0
    room[1][0] = temp

    temp = room[now[1]][c-1]
    for i in range(c-2, 0, -1):
        room[now[1]][i+1] = room[now[1]][i]
    
    temp2 = room[r-1][c-1]
    for i in range(r-1, now[1], -1):
        room[i][c-1] = room[i-1][c-1]
    room[now[1]+1][c-1] = temp

    temp = room[r-1][0]
    for i in range(c-1):
        room[r-1][i] = room[r-1][i+1]
    room[r-1][c-2] = temp2

    for i in range(now[1]+1, r-1):
        room[i][0] = room[i+1][0]
    room[now[1]][1] = 0
    room[r-2][0] = temp




dust_move = [(1,0), (-1,0), (0, 1), (0,-1)]
def spread(room):
    dust = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            d = room[i][j]
            spread = 0
            if d >= 5:
                for move in dust_move:
                    nx, ny = move[0]+i, move[1]+j

                    if nx < 0 or ny < 0 or nx >= r or ny >= c or room[nx][ny] == -1:
                        continue
                    # if room[nx][ny] != 0
                    spread += 1
                    dust[nx][ny] += d // 5
                
                room[i][j] = d - ((d // 5) * spread)
    
    for i in range(r):
        for j in range(c):
            room[i][j] += dust[i][j]

for _ in range(t):
    spread(room)
    circulate(room)

result = 0
for dust in room:
    result += sum(dust)

print(result+2)