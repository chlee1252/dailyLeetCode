memo = [0] * 1000
memo[1] = 1
memo[2] = 1
n = 100

for i in range(3, n+1):
   memo[i] = memo[i-1] + memo[i-2]



print(memo[n])