def findParent(parent, v1):
   if parent[v1] != v1:
      parent[v1] = findParent(parent, parent[v1])
   return parent[v1]

def union(parent, a, b):
   a = findParent(parent, a)
   b = findParent(parent, b)
   if a < b:
      parent[b] = a
   else:
      parent[a] = b

def solution(n, m, maps, plans):
   if len(plans) < 2:
      return "YES"
   
   # 초기 부모 테이블
   parent = [i for i in range(n+1)]
   for i in range(n):
      for j in range(n):
         if maps[i][j] == 1:
            union(parent, i+1, j+1)

   prev = findParent(parent, plans[0])
   for i in range(1, len(plans)):
      if prev != findParent(parent, plans[i]):
         return "NO"
   
   return "YES"



print(solution(5, 4, [[0,1,0,1,1], [1,0,1,1,0], [0,1,0,0,0], [1,1,0,0,0],[1,0,0,0,0]], [2,3,4,3]))
