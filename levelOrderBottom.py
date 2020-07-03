class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def levelOrderBottom(self, root: TreeNode) -> [[int]]:
    if not root: return []
    # First Approach: Recursion
    self.result = {}
    def traverse(root, index):
      if not root: return
      if index in self.result:
        self.result[index] += [root.val]
      else:
        self.result[index] = [root.val]
      
      traverse(root.left, index+1)
      traverse(root.right, index+1)

      return

    traverse(root, 0)
    return [self.result[i] for i in range(len(self.result)-1, -1, -1)]

    # Second Approach: Iterative
    # res = []
    # queue = [root]

    # while queue:
    #   level = []
    #   size = len(queue)

    #   for _ in range(size):
    #     node = queue.pop(0)
    #     if node:
    #       level.append(node.val)
    #       queue.append(node.left)
    #       queue.append(node.right)
      
    #   if level:
    #     res.insert(0, level)
    
    # return res
  