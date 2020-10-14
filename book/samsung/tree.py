from collections import defaultdict, deque

n, m, k = map(int, input().split())

moves = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]

food = [[5] * (n+1) for _ in range(n+1)]
original = [list(map(int, input().split())) for _ in range(n)]
tree = defaultdict(deque)
tree_count = m

for _ in range(m):
    x, y, age = map(int, input().split())
    tree[(x,y)].append(age)

def solve():
    global tree_count
    for x in range(n*n):
        i, j = (x//n)+1, (x%n)+1
        # 겨울
        if not tree[(i,j)]:
            food[i][j] += original[i-1][j-1]
            continue

        # 봄 & 여름
        tmp = deque([])
        add_food = 0
        while tree[(i,j)]:
            t = tree[(i,j)].pop()

            # 여름 -> 나중에 업데이트 해야함
            if food[i][j] < t:
                add_food += (t // 2)
                tree_count -= 1
                continue

            food[i][j] -= t
            t += 1
            tmp.append(t)

        tree[(i,j)] = sorted(tmp, reverse=True)

        food[i][j] += add_food
        food[i][j] += original[i-1][j-1]
            
    
    tmp_tree = defaultdict(list)
    for key, value in tree.items():
        spread = 0
        for v in value:
            if v < 5:
                break
            if v % 5 == 0:
                spread += 1
                
        if spread > 0:
            x, y = key
            for move in moves:
                nx, ny = move[0]+x, move[1]+y
                if 1 <= nx <= n and 1 <= ny <= n:
                    tree[(nx, ny)].extend([1] * spread)
                    tree_count += spread
            
for _ in range(k):
    solve()

print(tree_count)
