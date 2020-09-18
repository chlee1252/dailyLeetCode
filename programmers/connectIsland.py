def solution(n, costs):
  costs.sort(key=lambda x: x[2])
  visited = [0] * n
  visited[0] = 1
  answer = 0
  while 0 in visited:
    for cost in costs:
      b, e, c = cost

      if visited[b] == 1 and visited[e] == 1:
        continue

      if visited[b] or visited[e]:
        visited[b] = 1
        visited[e] = 1
        answer += c
        break
  
  return answer

print(solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]))