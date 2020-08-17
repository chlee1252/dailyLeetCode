class Solution:
	def distributionCandies(self, candies: int, num_people: int) -> [int]:
		run = 0
		out = [0] * num_people
		while candies:
			for i in range(num_people):
				temp_increment = min(candies, run * num_people + (i+1))
				out[i] += temp_increment
				candies -= temp_increment
				if candies == 0: return(out)
			run += 1

