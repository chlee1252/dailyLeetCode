class Solution:
  def maxAreaOfIsland(self, grid: [[int]]) -> int:
    # Breadth First Search Algorithm
    ans = 0
    iMax, jMax = len(grid), len(grid[0])

    for i in range(iMax):
      for j in range(jMax):
        if grid[i][j] == 1:
          size = self.bfs(i, j, iMax, jMax, grid, 0)
          ans = max(ans, size)
      
    return ans
  
  def bfs(self, i, j, iMax, jMax, grid, ans):
    # Check if i, j is inside the board, and grid[i][j] == 0
    if i < 0 or j < 0 or i >= iMax or j >= jMax or grid[i][j] == 0:
      return ans
    
    grid[i][j] = 0
    ans += 1

    ans = self.bfs(i+1, j, iMax, jMax, grid, ans)
    ans = self.bfs(i-1, j, iMax, jMax, grid, ans)
    ans = self.bfs(i, j-1, iMax, jMax, grid, ans)
    ans = self.bfs(i, j+1, iMax, jMax, grid, ans)

    return ans