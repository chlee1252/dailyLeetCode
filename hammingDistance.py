class Solution:
  def hammingDistance(self, x: int, y: int) -> int:
    # Approach 1:
    # if x == y:
    #   return 0
    # else:
    #   z = x ^ y
    #   z = bin(z)
    #   return z.count('1')
    # Approach 2:

    x = x ^ y
    y = 0
    while x:
      y += 1
      y = x & (x - 1)
    
    return y