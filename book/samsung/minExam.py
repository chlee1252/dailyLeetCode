from collections import defaultdict

n = int(input())
room = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
hash = defaultdict(int)

for i in room:
    if not hash[i]:
        tmp = i - b
        if tmp > 0:
            if tmp % c != 0:
                hash[i] = (tmp // c) + 2
            else:
                hash[i] = (tmp // c) + 1
        else:
            hash[i] = 1

    answer += hash[i]
    
print(answer) 