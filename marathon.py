from collections import Counter

def solution(participant, completion):
  part = Counter(participant)
  comp = Counter(completion)

  return list(part-comp)[0]