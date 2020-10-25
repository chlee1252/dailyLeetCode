from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens: [int], P: int) -> int:
        tokens.sort()
        q = deque(tokens)
        
        ans = bns = 0
        while q and (P >= q[0] or bns):
            while q and P >= q[0]:
                P -= q.popleft()
                bns += 1
            ans = max(ans, bns)
            
            if q and bns:
                P += q.pop()
                bns -= 1
        
        return ans