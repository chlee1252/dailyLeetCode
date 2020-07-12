class Solution:
  def subsets(self, nums:[int]) -> [[int]]:
    res = [[]]

    for n in nums:
      for i in range(len(res)):
        res.append(res[i] + [n])
    
    return res