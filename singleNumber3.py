from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        AXORB = reduce(lambda x, y: x^y, nums)
        mask = AXORB & -AXORB
        groupA = 0
        groupB =0
        for n in nums:
            if n & mask:
                groupA ^= n
            else:
                groupB ^= n
        return [groupA, groupB]