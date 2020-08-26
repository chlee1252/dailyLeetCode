class Solution:
  def heightChecker(self, heights: [int]) -> int:
    # 1-liner
    return sum(i != j for i, j in zip(heights, sorted(heights)))

    # for loop
    # count = 0
    # for i, j in zip(heights, sorted(heights)):
    #   if i != j:
    #     count += 1
    
    # return count