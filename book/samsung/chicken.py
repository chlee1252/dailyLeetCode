# 완전 탐색으로 풀기

from itertools import combinations

n, m = map(int, input().split())

town = []
chicken_pos = []

for _ in range(n):
    town.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if town[i][j] == 2:
            chicken_pos.append((i,j))

def calc_distance(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1-y2)

result = list(combinations(chicken_pos, m))

cur_dist = float('inf')
for chicken in result:
    dist = 0
    for i in range(n):
        for j in range(n):
            tmp_dist = float('inf')
            if town[i][j] == 1:
                for c in chicken:
                    cx, cy = c
                    tmp_dist = min(tmp_dist, calc_distance(i, cx, j, cy))
                dist += tmp_dist
    
    cur_dist = min(dist, cur_dist)

print(cur_dist)

