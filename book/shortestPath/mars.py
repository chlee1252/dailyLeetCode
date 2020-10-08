import heapq

tests = int(input())
INF = float("inf")
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(tests):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    distance = [[INF] * (n+1) for _ in range(n+1)]
    
    distance[0][0] = graph[0][0]
    q = [(graph[0][0], 0, 0)]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for move in moves:
            nx, ny = move[0]+x, move[1]+y
            if nx < 0 or ny < 0 or ny >= n or nx >= n:
                continue
            
            cost = graph[nx][ny] + dist
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])


'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

'''