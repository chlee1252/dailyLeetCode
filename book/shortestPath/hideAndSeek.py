import heapq

n, m = map(int, input().split())
INF = float("inf")

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 인거 까먹지 말것!
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance[1] = 0
q = [(distance[1], 1)]

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

a, b, c = -1, max(distance[1:]), 0

for i in range(1, n+1):
    if distance[i] == b:
        c += 1
        if a == -1:
            a = i

print(a, b, c)

# a = 0
# b = 0
# c = []

# for i in range(1, n+1):
#     if distance[i] > b:
#         a = i
#         b = distance[i]
#         c = [i]
#     elif distance[i] == b:
#         c.append(i)

# print(a, b, len(c))


'''
입력값 예시
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''

