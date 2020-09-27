from collections import Counter

def solution(N, stages):
    total_player = len(stages)
    hash = Counter(stages)

    answer = [hash[1] / total_player]
    for i in range(2, N+1):
        total_player -= hash[i-1]
        if total_player == 0:
            answer.append(0)
        else:
            answer.append(hash[i] / total_player)

    return [i[0]+1 for i in sorted(enumerate(answer), key=lambda x: x[1], reverse=True)]