class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def widthOfBinaryTree(self, root: TreeNode) -> int:
    ans = 0
    queue = [(root, 0)]

    while queue:
      _queue = []
      if queue:
        ans = max(ans, queue[-1][1] - queue[0][1] + 1)
      
      for node, index in queue:
        if node.left:
          _queue += [(node.left, index * 2 + 1)]
        if node.right:
          _queue += [(node.right, index * 2 + 2)]

      queue = _queue
    
    return ans

    # Approach 2:

    # queue = [(root, 0)]
    # max_width = 0

    # while queue:
    #   temp = []
    #   left = float('inf')
    #   right = float('-inf')
    #   for node, depth in queue:
    #     left = min(left, depth)
    #     right = max(right, depth)

    #     if node.left:
    #       temp.append((node.left, 2 * depth))
    #     if node.right:
    #       temp.append((node.right, 2 * depth + 1))
      
    #   max_width = max(max_width, right-left+1)
    #   queue = temp
    
    # return max_width