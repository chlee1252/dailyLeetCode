# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         self.count = 0
#         if not root:
#             return self.count
        
#         def dfs(root):
#             if not root:
#                 return
            
#             self.count += 1
            
#             dfs(root.left)
#             dfs(root.right)
            
#             return
        
#         dfs(root)
        
#         return self.count
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        ''' 3. Compare the heights of left & right tree. 
        If lh == rh => left tree is perfect
        Else => right tree is perfect
        '''
        def get_height(node):
            return -1 if not node else 1 + get_height(node.left)
        
        if not root:
            return 0
        
        lh = get_height(root.left)
        rh = get_height(root.right)
        
        if lh == rh: # Left tree is perfect
            return 1 + pow(2, lh+1)-1 + self.countNodes(root.right)
        else:
            return 1 + pow(2, rh+1)-1 + self.countNodes(root.left)