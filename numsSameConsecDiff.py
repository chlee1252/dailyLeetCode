class Solution:
	def numsSameConsecDiff(self, N: int, K: int) -> [int]:
		cur = range(10)
		for i in range(N-1):
			cur = {x * 10 + y for x in cur for y in [x % 10 + K, x % 10 - K] if x and 0 <= y < 10}
		return list(cur)

