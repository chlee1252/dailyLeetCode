from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        wnd, res = [], []
        for i, num in enumerate(nums):
            if i >= k and wnd[0] <= i - k:
                wnd.pop(0)
            while wnd and nums[wnd[-1]] <= num:
                wnd.pop()
            wnd.append(i)
            
            if i >= k - 1:
                res.append(nums[wnd[0]])
        return res