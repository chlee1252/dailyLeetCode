def solution(N, K):
    answer = 0
    while N % K != 0:
        N -= 1
        answer += 1
    while N != 1:
        N = N // K
        answer += 1

    while N > 1:
        N -= 1
        answer += 1
    
    return answer


assert solution(17, 4) == 3
assert solution(25, 5) == 2
        
