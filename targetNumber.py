def solution(numbers: [int], target: int):
  # Approach 1: Recursive Solution
  # if not numbers and target == 0:
  #   return 1
  # elif not numbers:
  #   return 0
  # else:
  #   return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
  # Approach 2: Iterative Solution
  tree = [0]
  for n in numbers:
    subTree = []
    for t in tree:
      subTree.append(t+n)
      subTree.append(t-n)
    tree = subTree
  
  return tree.count(target)
