class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n).replace("0b", "") # convert given number to binary representation
        if (len(s) != 32): # Check if the binary string is 32 bits
            s = "0"*(32 - len(s)) + s
        s = s[::-1] # reverse the string
        return int(s, 2)