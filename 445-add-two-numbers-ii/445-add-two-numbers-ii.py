# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def convertToString(l):
            num = ''
            while l:
                num += str(l.val)
                l = l.next
                
            return num
        
        num1 = convertToString(l1)
        num2 = convertToString(l2)
        
        num3 = int(num1) + int(num2)
        num3 = str(num3)
        
        dummy = curr = ListNode(0)
        
        for i in num3:
            curr.next = ListNode(int(i))
            curr = curr.next
            
        return dummy.next
        
        
        