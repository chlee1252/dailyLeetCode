class Solution:
    def twoCitySchedCost(self, costs:[[int]]) -> int:
        limit = len(costs) // 2   # Calculate half length
        costs.sort(key=lambda p: p[0] - p[1])
        A = sum(map(lambda p: p[0], costs[:limit]))
        B = sum(map(lambda p: p[1], costs[limit:]))

        return A + B

s = Solution()
print(s.twoCitySchedCost([[10,20], [30,200], [400,50], [30,20]]))

