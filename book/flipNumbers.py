def solution(S):
   count0 = 0
   count1 = 0
   if S[0] == '1':
      count0 += 1
   else:
      count1 += 1
   
   for i in range(len(S) - 1):
      if S[i] != S[i+1]:
         if S[i+1] == '1':
            count0 += 1
         else:
            count1 += 1
   
   return min(count0, count1)

print(solution("0001100"))
print(solution("0110"))
print(solution("0101010101010101010"))