class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two pointers
        if len(nums) == 0: return 0
        i = 0
        
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        
        return i+1


#         # Actually remove
#         if len(nums) == 0: return 0
    
#         i = 0
        
#         while i < len(nums)-1:
#             if nums[i] == nums[i+1]:
#                 del nums[i+1]
#             else:
#                 i += 1
        
#         return len(nums)
        