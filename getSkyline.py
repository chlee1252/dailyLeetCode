from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq
        events = sorted([(l, -h, r) for l,r,h in buildings] + [(r, 0, None) for _,r,_ in buildings])
        res = [[0,0]] # [x, h]
        heap = [(0, float('inf'))] # (h, end)
        for x, h, end in events:
            while x >= heap[0][1]:
                heapq.heappop(heap)
            if h:
                heapq.heappush(heap, (h, end))
            if res[-1][1] != -heap[0][0]:
                res.append([x, -heap[0][0]])
        return res[1:]