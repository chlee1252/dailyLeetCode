class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if not head:
      return
      
    length = 0
    h = head
    while h:
      h = h.next
      length += 1
    
    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy

    newN = length - n

    for i in range(newN):
      cur = cur.next
    
    cur.next = cur.next.next

    return dummy.next
