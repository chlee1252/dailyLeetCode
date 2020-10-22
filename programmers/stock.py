def solution(prices):
    stack = []
    n = len(prices)
    answer = [0] * n
    for i in range(1, n+1):
        while stack and stack[-1][0] > prices[i-1]:
            p, j = stack.pop()
            newJ = abs(i - j)
            answer[j-1] = newJ
        stack.append((prices[i-1], i))
    
    if stack:
        while stack:
            p, i = stack.pop()
            answer[i-1] = abs(n-i)
            
    return answer

print(solution([1,2,3,2,3]))