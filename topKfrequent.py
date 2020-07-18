from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        if len(nums) == 1:
            return nums
        
        hash = Counter(nums)
        hash = {k: v for k, v in sorted(hash.items(), key=lambda item: item[1], reverse=True)}

        return list(hash.keys())[:k]
        
        