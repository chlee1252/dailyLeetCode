from collections import Counter

class Solution:
  def longestPalindrome(self, s: str) -> int:
    odds = sum([freq % 2 for _, freq in Counter(s).items()])
    if odds <= 1:
      return len(s)
    else:
      return len(s) - odds + 1

  
s = Solution()
print(s.longestPalindrome("abccccdd"))