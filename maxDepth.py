# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.max = 0
        def dfs(root, depth):
            if not root:
                return
            
            if not root.left and not root.right:
                self.max = max(self.max, depth)
                return
            
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
            
            return
        
        dfs(root, 1)
        return self.max
            
        