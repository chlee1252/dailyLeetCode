class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [1] + [int(str((10**10+1)**rowIndex)[-10*(i+1):-10*i]) for i in range(1,rowIndex+1)]
