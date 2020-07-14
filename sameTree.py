class TreeNode:
  def __init__(self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
      return True
    
    if not p or not q:
      return False
    
    if p.val != q.val:
      return False
    
    return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

