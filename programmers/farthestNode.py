from collections import defaultdict, deque

def solution(N, edge):
   dists = {i: 0 for i in range(1, N+1)}      # 거리를 저장할 테이블
   nodes = defaultdict(list)                  # 특정 노드의 인접노드를 저장할 테이블

   # 양방향 그래프이기 때문에 양쪽 다 저장
   for i, j in edge:
      nodes[i] += [j]
      nodes[j] += [i]

   queue = deque(nodes[1])
   dist = 1
   
   # 근접 노드부터 탐색 하기 위해 BFS사용
   while queue:
      for i in range(len(queue)):
         node = queue.popleft()
         
         # 노드가 한번도 방문하지 않았을때,
         if dists[node] == 0:
            dists[node] = dist
            queue += deque(nodes[node])
      
      dist += 1
   
   del dists[1]    # 1부터 시작 했기 때문에 1은 제외 

   maxVal = max(dists.values())
   answer = 0
   for k in dists:
      if dists[k] == maxVal:
         answer += 1
   
   return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))