class Solution:
    def reverseString(self, s: [str]) -> None:
        # Approach 1: Without using built-in reverse() function
        first, last = 0, len(s)-1

        while first < last:
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1

        # Approach 2: Use built-in reverse() function
        # s.reverse()
