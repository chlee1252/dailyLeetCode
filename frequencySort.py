from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # Version 1: Using Counter (1 line)
        return "".join(i * v for i,v in Counter(s).most_common())
        
        #Version 2: Original Dictionary (7 lines)
#         hash = {}
#         for char in s:
#             if char in hash:
#                 hash[char] += 1
#             else:
#                 hash[char] = 1
        
#         return "".join(i * v for i,v in sorted(hash.items(), key=lambda item: item[1], reverse=True))