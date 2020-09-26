import math

class Solution:
    def maxProduct(self, nums: [int]) -> int:
        mini, maxi, res = 1, 1, -math.inf
        for n in nums:
            a = mini * n
            b = maxi * n
            mini = min(a, b, n)
            maxi = max(a, b, n)
            res = max(res, maxi)
        return res