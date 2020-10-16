n = int(input())
team = [list(map(int, input().split())) for _ in range(n)]

current = [False] * n
answer = float('inf')

def solve(count, index):
    global answer
    
    if index == n:
        return
    
    if count == n // 2:
        first, second = 0, 0
        for i in range(n):
            for j in range(n):
                if current[i] and current[j]:
                    first += team[i][j]
                elif not current[i] and not current[j]:
                    second += team[i][j]
        
        answer = min(answer, abs(first-second))
        return
    
    current[index] = True
    solve(count+1, index+1)
    current[index] = False
    solve(count, index+1)

solve(0,0)
print(answer)

