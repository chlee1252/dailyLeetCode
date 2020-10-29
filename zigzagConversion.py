class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res, gap = "", 2*(numRows-1)
        for i in range(numRows):
            tmp = i
            while tmp < len(s):
                res += s[tmp]
                # special cases 
                if i != 0 and i != numRows-1: 
                    if tmp+gap-2*i < len(s):
                        res += s[tmp+gap-2*i]
                tmp += gap
        return res