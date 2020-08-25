class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        # Approach 1
        beg, end = 0, len(A) - 1
        
        while beg <= end:
            if A[beg] % 2 == 0:
                beg += 1
            else:
                A[beg], A[end] = A[end], A[beg]
                end -= 1
        return A

        # Approach 2
        # A.sort(key=lambda a: a % 2)
        # return A

