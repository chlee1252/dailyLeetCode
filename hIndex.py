def solution(citations):
  citations.sort()
  indexes = []
  for i in range(len(citations)):
    if citations[i] >= len(citations[i:]):
      indexes.append(len(citations[i:]))
  
  if not indexes: return 0
  return max(indexes)