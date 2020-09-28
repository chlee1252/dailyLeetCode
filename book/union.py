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


def algorithm(v, unionNodes):
   # parent 테이블 생성 (초기: 자기 자신을 부모로 설정)
   parent = [i for i in range(v+1)]

   print(parent) 

   # Union실행
   for a, b in unionNodes:
      union(parent, a, b)

   for i in range(v+1):
      print(findParent(parent, i), end= ' ')
   print()
   for i in range(1, v+1):
      print(parent[i], end=' ')

algorithm(6, [(1,4), (2,3), (2,4), (5,6)])
