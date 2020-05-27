class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        count = 0
        result = 0
        path = {0:0}        #key = count, value = index
        
        for i, v in enumerate(nums, 1):
            if v == 0:
                count += 1
            else:
                count -= 1
            
            if count in path:
                result = max(result, i - path[count])
            else:
                path[count] = i
        
        return result