def solution(N):
   N = str(N)

   first, last = list(map(int,N[:len(N)//2])), list(map(int, N[len(N)//2:]))
   
   if sum(first) == sum(last):
      return 'LUCKY'
   
   return 'READY'

print(solution(123402))
print(solution(7755))