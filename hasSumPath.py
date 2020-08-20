from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
  def hasSumPath(self, root: TreeNode, sum: int) -> bool:
    # Approach 1: DFS with Recursion
    if not root:
      return False
    
    self.result = False
    def dfs(root, val):
      if not root:
        return
      
      new_val = val + root.val
      if not root.left and not root.right:
        if new_val == sum:
          self.result = True
          return
      
      dfs(root.left, new_val)
      dfs(root.right, new_val)

      return
    
    dfs(root, 0)

    return self.result

    # Approach 2: Iterative
    # if not root:
    #   return False
    # stack = deque([(root, sum - root.val)])

    # while stack:
    #   node, val = stack.pop(0)
    #   if not node.left and not node.right and val == 0:
    #     return True
      
    #   if node.left:
    #     stack.append((node.left, val - node.left.val))
      
    #   if node.right:
    #     stack.append((node.right, val - node.right.val))
    
    # return False
