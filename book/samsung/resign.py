n = int(input())
# n = 7
# p = [3,5,1,1,2,4,2]
# q = [10,20,10,20,15,40,200]

p, q = [0]*n, [0]*n
for i in range(n):
    p[i], q[i] = map(int, input().split())

dp = [0]*25

for i in range(n):
    dp[i+1] = max(dp[i], dp[i+1])

    if dp[i+p[i]] < dp[i]+q[i]:
        dp[i+p[i]] = dp[i]+q[i]

print(dp[n])