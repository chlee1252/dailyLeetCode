from collections import deque, defaultdict

def getDest(dest):
    q = deque([(ti,tj, 0)])
    di, dj = dest
    visited = {(ti, tj)}

    while q:
        i, j, cost = q.popleft()
        if i == di and j == dj:
            return (i, j, cost)
        
        for move in moves:
            ni, nj = i+move[0], j+move[1]

            if ni < 0 or nj < 0 or ni >= n or nj >= n or (ni, nj) in visited or world[ni][nj] == 1:
                continue

            visited.add((ni, nj))
            q.append((ni, nj, cost+1))
    
    return None

def findPassengers(dest):
    q = deque([(ti, tj, 0)])
    visited = {(ti, tj)}
    result = []

    while q:
        i, j, cost = q.popleft()
        if (i, j) in dest:
            result.append((i,j, cost))

        for move in moves:
            ni, nj = i+move[0], j+move[1]

            if ni < 0 or nj < 0 or ni >= n or nj >= n or (ni, nj) in visited or world[ni][nj] == 1:
                continue
            
            visited.add((ni, nj))            
            q.append((ni, nj, cost+1))
    if result:
        result.sort(key=lambda x: (x[2], x[0], x[1]))
        return result[0]
    
    return result
    
def solve():
    global fuel, ti, tj, passengers
    numb = 0
    while numb < m:
        dist = findPassengers(passengers)
        if not dist:
            return -1
                
        # 승객 태우러 가는 비용
        ti, tj, cost = dist
        fuel -= cost

        if fuel < 0:
            return -1

        # 목적지까지
        tmp = getDest(passengers[(ti, tj)])
        if tmp:
            i, j, cost = tmp
            fuel -= cost
        else:
            return -1

        # 손님 지우기
        passengers.pop((ti, tj), None)
        
        if fuel < 0:
            return -1
        
        ti, tj = i, j
        fuel += (cost * 2)
        numb += 1
    
    return fuel

    

if __name__ == "__main__":
    n, m, fuel = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(n)]
    ti, tj = map(int, input().split())
    ti, tj = ti-1, tj-1
    passengers = defaultdict(tuple)
    for _ in range(m):
        s1, s2, d1, d2 = map(int, input().split())
        passengers[(s1-1, s2-1)] = (d1-1, d2-1)

    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    print(solve())

