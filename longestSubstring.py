class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        self.ans = 0
        def helper(s):
            if(len(s)<=self.ans):return
            Table = Counter(s)
            forbiden=set()
            for c in Table:
                if(Table[c]<k):forbiden.add(c)
            if(not forbiden):
                self.ans=len(s)
                return
            while(s and s[0] in forbiden):s=s[1:]
            if(not s):return
            pre=0
            for i,c in enumerate(s):
                if(c in forbiden):
                    helper(s[pre:i])
                    pre=i+1
            helper(s[pre:])
        helper(s)
        return self.ans