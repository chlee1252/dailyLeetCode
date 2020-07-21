class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    dummy = prev = ListNode()
    dummy.next = head

    while head:
      if head.val == val:
        prev.next = head.next
      else:
        prev = prev.next
      head = head.next
    
    return dummy.next
