def solution(begin, target, words):
  answer = 0
  if target not in words:
    return 0
  
  # dfs: finding route (depth)
  stack = [begin]
  visited = [0] * len(words)

  while stack:
    node = stack.pop()

    if node == target:
      break

    for i in range(len(words)):
      word = words[i]
      diff = 0
      for j in range(len(word)):
        if word[j] != node[j]:
          diff += 1
      
      if diff == 1:
        if visited[i] == 0:
          visited[i] = 1
          stack.append(word)
    
    answer += 1
  
  return answer
