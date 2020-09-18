from collections import deque

def solution(n, computers):
  answer = 0
  visited = [0] * n
  queue = deque([])

  while 0 in visited:
    index = visited.index(0)
    queue.append(index)
    visited[index] = 1

    while queue:
      node = queue.popleft()

      for i in range(n):
        if visited[i] == 0 and computers[node][i] == 1:
          visited[i] = 1
          queue.append(i)
    
    answer += 1
  
  return answer

print(solution(3, [[1,1,0],[1,1,0],[0,0,1]]))