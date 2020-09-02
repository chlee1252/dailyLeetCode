class Solution:
  def solution(self, answers):
    pattern = {1: [1,2,3,4,5], 2: [2,1,2,3,2,4,2,5], 3: [3,3,1,1,2,2,4,4,5,5]}
    person = {1: 0, 2: 0, 3: 0}
    maximum = 0

    for i in range(len(answers)):
      if pattern[1][i % len(pattern[1])] == answers[i]:
        person[1] += 1
      
      if pattern[2][i % len(pattern[2])] == answers[i]:
        person[2] += 1
      
      if pattern[3][i % len(pattern[3])] == answers[i]:
        person[3] += 1

      maximum = max(maximum, person[1], person[2], person[3])

    return [k for k, v in person.items() if v == maximum]

  
s = Solution().solution([1,2,3,4,5])

print(s)


