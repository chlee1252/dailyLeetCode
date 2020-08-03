import re

class Solution:
  def isPalindrome(self, s: str) -> bool:
    if len(s) == 0 or len(s) == 1:
      return True
    
    # Method 1: Without using regex
    s = ''.join(e for e in s if e.isalnum()).lower()

    # Method 2: Using regex
    # s = ''.join(re.findall('[A-Za-z0-9]', s)).lower()

    return s == s[::-1]