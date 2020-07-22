class Solution:
  def dfs(self, x: int, y: int, xMax: int, yMax:int, board: [[str]], word: str) -> bool:
    # Initial
    if not word:
      return True

    # Check Boundary
    if x < 0 or y < 0 or x >= xMax or y >= yMax or board[x][y] != word[0]:
      return False
    
    tmp = board[x][y]
    board[x][y] = "#"           # Mark as a Visited node
    newWord = word[1:]

    res = self.dfs(x+1, y, xMax, yMax, board, newWord) \
          or self.dfs(x-1, y, xMax, yMax, board, newWord) \
          or self.dfs(x, y+1, xMax, yMax, board, newWord) \
          or self.dfs(x, y-1, xMax, yMax, board, newWord)
    
    board[x][y] = tmp

    return res

  def exist(self, board: [[str]], word: str) -> bool:
    if not board:
      return False
    
    xMax, yMax = len(board), len(board[0])

    for x in range(xMax):
      for y in range(yMax):
        if board[x][y] == word[0]:
          if self.dfs(x, y, xMax, yMax, board, word):
            return True
      
    return False