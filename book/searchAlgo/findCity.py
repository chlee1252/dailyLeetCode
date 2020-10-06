from collections import deque, defaultdict

N, M, K, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)


# bfs
visited = [False] * (N+1)
q = deque([(X, 0)])
visited[X] = True
result = []
while q:
    v, dist = q.popleft()

    if dist == K:
        result.append(v)
    
    for i in graph[v]:
        if not visited[i]:
            q.append((i, dist+1))
            visited[i] = True

if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)

