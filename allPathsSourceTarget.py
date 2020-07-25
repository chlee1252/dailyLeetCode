from collections import deque

class Solution:
  def allPathsSourceTarget(self, graph: [[int]]) -> [[int]]:
    res = []
    if not graph:
      return res
    
    queue = deque([(0, [0])])

    while queue:
      idx, path = queue.popleft()

      if idx == len(graph) - 1:
        res.append(path)
      else:
        for i in graph[idx]:
          queue.append((i, path + [i]))
      
    return res