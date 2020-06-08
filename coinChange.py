class Solution:
  def change(self, amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in coins:
      for j in range(j, amount+1):
        dp[j] += dp[j - i]
    
    return dp[amount]