class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        # iterate
        stack = []
        result = root.val
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1
            
            if k == 0:
                return root.val
            
            root = root.right
            
        #recursive
        self.result = root.val
        self.k = k
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.result = root.val
                return
            dfs(root.right)
        
        dfs(root)
        
        return self.result