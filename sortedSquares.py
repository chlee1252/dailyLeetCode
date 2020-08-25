class Solution:
  def sortedSquares(self, nums: [int]) -> [int]:
    # Approach 1: use sort() and for loop
    A.sort(key=lambda a: a ** 2)
    for i in range(len(A)):
      A[i] = A[i] ** 2
    
    return A

    # Approach 2: use sorted()
    # return sorted(i ** 2 for i in A)
