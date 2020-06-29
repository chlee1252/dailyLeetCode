class Solution:
  def findItinerary(self, tickets:[[str]]) -> [str]:
    from collections import deque
    graph = {}
    for ticket in tickets:
      graph[ticket[0]] = graph.get(ticket[0], []) + ticket[1]

    for start in graph:
      graph[start] = deque(sorted(graph[start]))
    
    def dfs(root, graph, path, maxLen):
      if len(path) == maxLen:
        return True
        
      for k in range(len(graph.get(root,[]))):
        end = graph[root].popleft()
        path.append(end)

        if dfs(end, graph, path, maxLen):
          return True
          
        path.pop()
        graph[root].append(end)
    path = ["JFK"]
    dfs("JFK", graph, path, len(tickets) + 1)

    return path
      
      