"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        stack = []
        ans = head
        while head:
            if head.child:
                if head.next: stack.append(head.next)
                head.next = head.child
                head.child.prev = head
                head.child = None
                
            if not head.next:
                if stack:
                    node = stack.pop()
                    head.next = node
                    node.prev = head
                    
            head = head.next
        
        return ans
            