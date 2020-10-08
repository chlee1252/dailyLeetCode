def solution(N, coins):
   if 1 not in coins:
      return 1
   
   target = 1
   coins.sort()

   for coin in coins:
      if target < coin:
         break
      target += coin

   return target

print(solution(5, [1,2,4,7]))
print(solution(5, [3,2,1,1,9]))