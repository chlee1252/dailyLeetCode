from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        while (True):
            new = []
            j = 0
            for i in range(len(intervals)-1):
                if j > 0:
                    j -= 1
                    continue
                maxi = 0
                while (intervals[i][1] >= intervals[i+j+1][0]):
                    if intervals[i+j+1][1] > maxi:
                        maxi = intervals[i+j+1][1]
                    j += 1
                    if i+j+1 >= len(intervals):
                        break
                new.append([intervals[i][0], max(intervals[i+j][1], intervals[i][1], maxi)])
            if j == 0:
                new.append(intervals[-1])
            if len(new) == len(intervals):
                break
            else:
                intervals = new
        return new