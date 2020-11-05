class Solution:
    def minCostToMoveChips(self, chips: [int]) -> int:
        odd = len(list(filter(lambda v: v%2 == 1, chips)))
        even = len(chips) - odd
        return min(odd, even)