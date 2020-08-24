from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
class Solution:
  def sumOfLeftLeaves(self, root: TreeNode) -> int:
    if not root:
      return 0
    
    # Approach 1: Recursive
    self.result = 0
    def dfs(root: TreeNode, left: bool) -> None:
      if not root:
        return
      
      if not root.left and not root.right and left:
        self.result += root.val
      
      dfs(root.left, True)
      dfs(root.right, False)

      return
    
    dfs(root, False)
    return self.result

    # Approach 2: Iterative
    # result = 0
    # queue = deque([(root, False)])

    # while queue:
    #   node, isLeft = queue.popleft()

    #   if not node.left and not node.right and isLeft:
    #     result += node.val
    #     continue
      
    #   if node.left:
    #     queue.append((node.left, True))
    #   if node.right:
    #     queue.append((node.right, False))

    # return result
      
