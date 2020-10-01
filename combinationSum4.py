class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        candidates = sorted(candidates)
        results = [] 
        curr = [] 
        sum = 0

        def helper(idx: int):
            nonlocal results, curr, sum 
            if sum == target:
                results.append(list(curr))
                return 

            for jdx in range(idx, len(candidates)):
                if candidates[jdx] > target - sum:
                    return 
                sum += candidates[jdx]
                curr.append(candidates[jdx])
                helper(jdx) 
                sum -= curr.pop()

        helper(0)
        return results