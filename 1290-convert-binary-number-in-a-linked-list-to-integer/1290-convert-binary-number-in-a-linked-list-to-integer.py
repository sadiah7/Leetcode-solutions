# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        ls = []
        while head:
            count += 1
            ls.append(head.val)
            head = head.next
        
        op = 0
        for num in ls:
            # print(op, num*(2**(count-1)))
            op += num*(2**(count-1))
            count -= 1
        
        return op
               
        