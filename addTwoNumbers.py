class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # get the sum of the two numbers
        sumVal = self.toNumber(l1) + self.toNumber(l2)
        # split this result into a ListNode
        return self.fromNumber(sumVal)
    
    def toNumber(self, lNode):
        # traverse the linked list to get the individual digits
        intDigits = []
        while lNode is not None:
            intDigits.append(lNode.val)
            # get the next digit
            lNode = lNode.next
        # here we have a list of all the digits
        intDigits = list(map(str, intDigits))
        # convert to number
        return int(''.join(intDigits))
    
    def fromNumber(self, number):
        # split the number into individual digits
        number = str(number)
        lns = []
        # loop the rest to create the ListNodes
        for n in number:
            l = ListNode(int(n))
            # add to list
            lns.append(l)
            # set next for the previous node inf not first
            nodeCount = len(lns) 
            if nodeCount > 1:
                lns[nodeCount - 2].next = l
            
        # return the first node
        return lns[0]