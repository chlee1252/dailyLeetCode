def solution(S):
   s = list(S)
   s.sort()

   numbers = 0
   index = 0
   for i in range(len(s)):
      try:
         numbers += int(s[i])
         index = i
      except:
         break
   
   return ''.join(s[i:] + [str(numbers)])
   
print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))
