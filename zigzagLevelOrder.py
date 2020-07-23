from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
    if not root:
      return []
    
    queue = deque([root])
    res, direction = [], 1

    while queue:
      level = []
      for _ in range(len(queue)):
        node = queue.popleft()
        level.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
      
      res.append(level[::direction])
      direction *= -1
    
    return res
    