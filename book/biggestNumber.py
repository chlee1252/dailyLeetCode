def solution(N, M, K, array):
  array.sort()
  answer = 0

  continuous = 0
  for _ in range(M):
      if continuous == K:
        answer += array[N-2]
        continuous = 0
      else:
        answer += array[N-1]
        continuous += 1
      
    
  return answer


# print(solution(5, 7, 2, [3,4,3,4,3]))