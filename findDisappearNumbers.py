class Solution:
  def findDisappearNumbers(self, nums: [int]) -> [int]:
    # Extra Memory
    # extra = set(nums)
    # return [i for i in range(1, len(nums)+1) if i not in extra]

    # O(1) Memory
    for i in range(len(nums)):
      index = abs(nums[i]) - 1
      nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
