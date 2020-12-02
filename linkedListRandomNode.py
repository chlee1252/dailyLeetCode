import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.N = 0
        cur = head
        while cur:
            cur = cur.next
            self.N += 1
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        cur = self.head
        hops = random.randint(0, self.N-1)
        while hops:
            cur = cur.next
            hops -= 1
        
        return cur.val
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()