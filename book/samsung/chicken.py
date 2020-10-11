from itertools import combinations

n, m = map(int, input().split())
chicken = []
maps = []

def calc_distance(r1, r2, c1, c2):
    return abs(r1-r2) + abs(c1-c2)

for _ in range(n):
    maps.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken.append((i, j))
            maps[i][j] = 0

combo = list(combinations(chicken, m))

minDist = float('inf')
for i in range(len(combo)):
    distance = 0
    for c in range(n):
        for r in range(m):
            if maps[c][r] == 1:
                tmp = float('inf')
                for j in range(m):
                    tmp = min(tmp, calc_distance(r, combo[i][j][1], c, combo[i][j][0]))
                distance += tmp
    
    minDist = min(minDist, distance)

print(minDist)




