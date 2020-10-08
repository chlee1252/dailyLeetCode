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


def algorithm(v, nodes):
   # parent 테이블 생성 (초기: 자기 자신을 부모로 설정)
   parent = [i for i in range(v+1)]

   for a, b in nodes:
      if findParent(parent, a) == findParent(parent, b):
         return "Cycle!"
      else:
         union(parent, a, b)
   
   return "No Cylce!"

   

print(algorithm(3, [(1,2), (1,3), (2,3)]))
