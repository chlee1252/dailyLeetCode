def solution(N, M, cards):
  return max([min(card) for card in cards])


print(solution(3,3, [[3,1,2],[4,1,4],[2,2,2]]))
print(solution(2,4, [[7,3,1,8],[3,3,3,4]]))