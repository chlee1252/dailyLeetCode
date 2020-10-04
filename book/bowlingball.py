def solution(N, M, balls):
   # result = 0
   # for i in range(N):
   #    for j in range(i+1, N):
   #       if balls[i] != balls[j]:
   #          result += 1
   
   # return result

   result = 0
   array = [0] * 11

   for b in balls:
      array[b] += 1
   
   for i in range(1, M+1):
      N -= array[i]
      result += array[i] * N
   
   return result

print(solution(5, 3, [1,3,2,3,2]))
print(solution(8, 5, [1,5,4,3,2,4,5,2]))
