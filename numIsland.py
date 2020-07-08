class Solution:
  def numIsland(self, grid: [[str]]) -> int:
    # Breadth First Search
    ans = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == '1':
          ans += 1
          self.bfs(i, j, len(grid), len(grid[0]), grid)
    
    return ans
  
  def bfs(self, i, j, iMax, jMax, grid):
    if i < 0 or j < 0 or i >= iMax or j >= jMax or grid[i][j] == '0':
      return
    
    grid[i][j] = '0'

    self.bfs(i+1, j, iMax, jMax, grid)
    self.bfs(i-1, j, iMax, jMax, grid)
    self.bfs(i, j-1, iMax, jMax, grid)
    self.bfs(i, j+1, iMax, jMax, grid)

    return
