class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # Method 1: Without using loop for recursion
        # if num<= 0:
        #     return False
        # z = bin(num)[::-1]
        # if z.count('1') > 1:
        #     return False
        # p = z.index('1')
        # return p % 2 == 0 

        # Method 2: Use while loop 
        if num < 1:
            return False
        while num % 4 == 0:
            num /= 4
        return True if num == 1 else False
