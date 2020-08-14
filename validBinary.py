import math

class TreeNode:
  def __init__(self, val: int, left=None, right=None):
    self.left = left
    self.val = val
    self.right = right

class Solution:
  def isValidBST(self, root: TreeNode, floor=float('-inf'), ceiling=float('inf')) -> bool:
    if not root:
      return True

    if root.val <= floor or root.val >= ceiling:
      return False

    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)

