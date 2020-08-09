class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        queue = []
        fresh_cut = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_cut += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        minutes = 0
        while queue:
            size = len(queue)
            newly_rotten = []
            for i in range(size):
                v = queue.pop(0)
                x,y = v[0], v[1]
                for x2, y2 in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] == 1:
                        newly_rotten.append((x2, y2))
                        grid[x2][y2] = 2
                        fresh_cut -= 1
            
            if newly_rotten:
                queue.extend(newly_rotten)
                minutes += 1
        
        return minutes if fresh_cut == 0 else -1