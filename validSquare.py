from typing import *

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 or p2 == p3 or p3 == p4 or p4 == p1:
            return False
        x = [] 
        x.extend((p1, p2, p3, p4))
        x = sorted(x,key=lambda x:x[0])
        x = sorted(x,key=lambda x:x[1], reverse = True)
        p3 = x.pop()
        p4 = x.pop()
        p2 = x.pop()
        p1 = x.pop()
        return (math.sqrt((p1[0]-p3[0])**2 + (p1[1] - p3[1])**2) == math.sqrt((p2[0]-p4[0])**2 + (p2[1] - p4[1])**2)) and ( ( math.sqrt((p1[0]-p4[0])**2 + (p1[1] - p4[1])**2) == math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2) ) and ( math.sqrt((p3[0]-p4[0])**2 + (p3[1] - p4[1])**2) == math.sqrt((p3[0]-p2[0])**2 + (p3[1] - p2[1])**2) ) )