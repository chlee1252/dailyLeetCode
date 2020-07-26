class Solution:
    def findMin(self, nums: [int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi: 
            if nums[lo] < nums[hi]: 
                break 
            mid = (lo + hi)//2
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]: lo = mid + 1
            else: hi = mid
        return nums[lo]