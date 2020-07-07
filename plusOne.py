class Solution:
  def plusOne(self, digits: [int]) -> [int]:
    # Approach 1
    reverse = digits[::-1]
    for i in range(1, len(reverse) + 1):
      if reverse[i-1] < 9:
        digits[-1] = reverse[i-1] + 1
        break
      else:
        try:
          digits[-(i+1)] = digits[-(i+1)] + 1
          digits[-i] = 0
        except:
          digits[-1] = 0
          digits.insert(0, 1)
          break
    
    return digits

    # Approach 2
    # num = 1
    # for idx, val in enumerate(digits[::-1]):
    #   num += (x * 10 ** idx)
    # return list(str(num))