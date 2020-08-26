class Solution:
  def thirdMax(self, nums: [int]) -> int:
    dummy = [float('-inf'), float('-inf'), float('-inf')]

    for num in nums:
      if num not in dummy:
        if num > dummy[0]: dummy = [num, dummy[0], dummy[1]]
        elif num > dummy[1]: dummy = [dummy[0], num, dummy[1]]
        elif num > dummy[2]: dummy = [dummy[0], dummy[1], num]
    
    return max(nums) if float('-inf') in dummy else dummy[2]