def solution(N):
  change = [500, 100, 50, 10]
  answer = 0
  for coin in change:
    answer += (N // coin)
    N %= coin
  
  return answer


assert solution(1250) == 5
assert solution(1260) == 6
assert solution(0) == 0