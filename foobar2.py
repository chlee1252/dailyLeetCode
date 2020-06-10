def solution(x, y):
  answer = (((y+x-2)*(y+x-1))//2) + x
  return str(answer)

print(solution(5,10))