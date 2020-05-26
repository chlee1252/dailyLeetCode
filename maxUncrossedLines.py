class Solution:
    def maxUncrossedLines(self, A: [int], B: [int]) -> int:
        s = set(A) & set(B)
        A = [a for a in A if a in s]
        B = [b for b in B if b in s]
        m, n = len(A), len(B)
        if m < n:
            A, B, m, n = B, A, n, m
            
        dp = [0]*(m+1)                      # dp[i] in loop j: check up to A[i], B[j] 
        for j in range(n):                  # B[0]..B[j]
            new_dp = dp[:]
            for i in range(m):              # A[0]..A[i]
                if A[i] == B[j]:
                    new_dp[i+1] = dp[i] + 1 # add a new line
                else:
                    new_dp[i+1] = max(dp[i+1], new_dp[i])   # choose the best strategy
            dp = new_dp
            
        return dp[-1]