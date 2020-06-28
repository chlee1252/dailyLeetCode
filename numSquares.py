from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        while( n % 4 == 0 ):	# Reduction by factor of 4
            n /= 4
			
        if n % 8 == 7:			# If n = 8k + 7, returns 4
            return 4
			
        for a in range( int(sqrt(n))+1 ):	# Check if n = a^2 + b^2, return 0 / 1
            b = int(sqrt(n - a**2))
            if a**2 + b**2 == n:
                return (a>0) + (b>0)
				
        return 3				# If n = a^2 + b^2 + c^2, return 3