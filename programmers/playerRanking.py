from collections import defaultdict

def solution(n, results):
   # 인접해 있는 간선 정보
   win, lose = defaultdict(set), defaultdict(set)

   for result in results:
      win[result[0]].add(result[1])
      lose[result[1]].add(result[0])
   
   # 기본 그래프 그리기 끝
   

   # 명제: A선수의 실력이 B선수의 실력보다 좋으면 B는 A를 절대 이길 수 없다.
   # -> B선수에게 진 선수들도 A선수를 절대 이길 수 없다.
   # 명제를 토대로 관계 추가
   for i in range(1, n+1):
      # i선수를 이긴 선수들은 i가 이긴 선수들을 무조건 이긴다.
      for p in lose[i]:
         # p = i선수를 이긴 선수들
         win[p].update(win[i])
      
      # i선수에게 진 선수들은 절대 i선수를 이길 수 없다.
      for p in win[i]:
         # p = i선수에게 진 선수들
         lose[p].update(lose[i])
   
   answer = 0
   for i in range(1, n+1):
      if len(win[i]) + len(lose[i]) == n-1:
         answer += 1
   
   return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(4, [[1,2], [2,3], [3,4]]))
