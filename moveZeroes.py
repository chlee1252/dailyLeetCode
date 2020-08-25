class Solution:
  def moveZeroes(self, nums: [int]) -> None:
    lastNoneZeroIndex = 0
    for i in range(len(nums)):
      if nums[i] != 0:
        nums[lastNoneZeroIndex] = nums[i]
        lastNoneZeroIndex += 1
    
    for i in range(lastNoneZeroIndex, len(nums)):
      nums[i] = 0
  