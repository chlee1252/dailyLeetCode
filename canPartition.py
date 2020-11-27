from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
            s = sum(nums)
            if s % 2: return False
            target = s // 2

            dp = [0] * (target + 1)
            dp[0] = 1

            for current in nums:
                for new_target in range(target, current - 1, -1):
                    dp[new_target] = dp[new_target] or dp[new_target - current]

            return dp[target]