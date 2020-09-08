class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def sumRootToLeaf(self, root: TreeNode) -> int:
    if not root:
      return 0
    
    self.answer = 0

    def dfs(root, number):
      if not root:
        return 0

      number += str(root.val)

      if not root.left and not root.right:
        self.answer += int(number, 2)
        return
      
      dfs(root.left, number)
      dfs(root.right, number)

      return
    
    dfs(root, '')

    return self.answer
      