n = int(input())
numbers = list(map(int, input().split()))
add, sub, mult, div = map(int, input().split())

minimum, maximum = float('inf'), float('-inf')

def solve(answer, add, sub, mult, div, counter):
    global minimum, maximum
    if counter == n:
        minimum = min(minimum, answer)
        maximum = max(maximum, answer)
        return
    
    if add:
        solve(answer+numbers[counter], add-1, sub, mult, div, counter+1)
    
    if sub:
        solve(answer-numbers[counter], add, sub-1, mult, div, counter+1)

    if mult:
        solve(answer*numbers[counter], add, sub, mult-1, div, counter+1)
    
    if div:
        if answer < 0:
            solve(-(-answer // numbers[counter]), add, sub, mult, div-1, counter+1)
        else:
            solve(answer // numbers[counter], add, sub, mult, div-1, counter+1)

solve(numbers[0], add, sub, mult, div, 1)
print(maximum)
print(minimum)
