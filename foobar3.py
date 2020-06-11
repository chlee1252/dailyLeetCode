KNIGHT_MOVES = [(-2, -1), (-1, -2), (-1, 2), (-2, 1), (1, -2), (2, -1), (1, 2), (2, 1)] 
SIZE = 8

class Node:
  def __init__(self, x, y, dist=0):
    self.x = x
    self.y = y
    self.dist = dist
    self.visited = False
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
def createNode(n):
  return Node(int(n%8), int(n/8))

def isValid(x, y):
  return True if 0 <= x < SIZE and 0 <= y < SIZE else False

def bfs(src, dest):
  queue = [src]

  while queue:
    node = queue.pop(0)

    if node == dest:
      return node.dist
    
    for move in KNIGHT_MOVES:
      newX = node.x + move[0]
      newY = node.y + move[1]

      if isValid(newX, newY):
        queue.append(Node(newX, newY, dist=node.dist+1))

  return -1 




def solution(src, dest):
  srcNode = createNode(src)
  destNode = createNode(dest)
  return bfs(srcNode, destNode)
