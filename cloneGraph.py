
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if(not node):
            return 
        mapping = {} 
        q = [node]
        while(q):
            t = q.pop()
            if(t not in mapping):
                mapping[t] = Node(t.val)
            for n in t.neighbors:
                if(n not in mapping):
                    mapping[n] = Node(n.val)
                    q+=[n]
                mapping[t].neighbors+=[mapping[n]]
        return mapping[node]