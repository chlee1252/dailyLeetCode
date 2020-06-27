# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.result = 0
        if not root:
            return self.result
        
        def dfs(root, prev=0):
            if not root:
                return 
            
            temp = prev * 10 + root.val
            # Check leaf
            if not root.left and not root.right:
                self.result += temp
            
            dfs(root.left, temp)
            dfs(root.right, temp)
            
            return
        
        dfs(root)
        
        return self.result
            