from collections import defaultdict, Counter
from functools import reduce

def solution(clothes):
  # Approach 1: use defaultdict
  answer = 1              # Set init answer value as 1
  hash = defaultdict(int)

  for cloth in clothes:
    hash[cloth[1]] += 1
  
  for key, value in hash.items():
    answer *= value + 1
  
  return answer-1         # Remove init answer value

  # Approach 2: Use Counter and reduce(function, iterable, init), Better and clean approach

  hash = Counter([kind for name, kind in clothes])

  return reduce(lambda x, y: x*(y+1), hash.values(), 1) - 1

