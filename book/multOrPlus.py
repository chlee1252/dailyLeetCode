def solution(S):
   result = 0
   for num in S:
      num = int(num)     
      if num < 2 or result < 2:
         result += num
      else:
         result *= num
      
      # print(result) 
   
   return result

print(solution("1111"))
print(solution("011111"))
print(solution("567"))
print(solution("02984"))
print(solution("012"))