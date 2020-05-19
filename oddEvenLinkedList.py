def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head
        even = head.next
        odd = head
        evenHead = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenHead
        
        return head