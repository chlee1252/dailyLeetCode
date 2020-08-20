class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
  # Approach 1: Recursive Solution
  def isSymmetricRecursive(self, root: TreeNode) -> bool:
    def isSym(L: TreeNode, R: TreeNode) -> bool:
      if L and R and L.val == R.val:
        return isSym(L.left, R.right) and isSym(L.right, R.left)
      return L == R
    
    return not root or isSym(root.left, root.right)

  # Approach 2: Iterative Solution
  def isSymmetric(self, root: TreeNode) -> bool:
    queue = [root]
    while queue:
        values = [i.val if i else None for i in queue]
        if values != values[::-1]: return False
        queue = [child for i in queue if i for child in (i.left, i.right)]
    return True