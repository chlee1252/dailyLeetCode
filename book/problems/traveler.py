def solution(N, members):
   result = 0
   member = 0
   members.sort()

   for m in members:
      member += 1
      if m <= member:
         result += 1
         member = 0
   
   return result

print(solution(5, [2,3,1,2,2]))
         
