class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        # Approach 1: Binary Search O(log n)
        l, r = 0, len(nums)

        while l < r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                r = mid
            else:
                l = mid + 1

        return l
        
        # Approach 2: Brute Force O(n)
        
        #if target < nums[0]: return 0
        #for i, v in enumerate(nums):
        #    if v == target: return i
            
        #    if i+1 == len(nums) or v < target < nums[i+1]:
        #        return i+1
        
