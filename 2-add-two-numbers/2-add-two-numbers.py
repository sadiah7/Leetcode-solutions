# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(-1)
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            if total > 9:
                cur.next = ListNode(total - 10)
                carry = 1
            else:
                cur.next = ListNode(total)
                carry = 0
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + carry
            if total > 9:
                cur.next = ListNode(total - 10)
                carry = 1
            else:
                cur.next = ListNode(total)
                carry = 0
            cur = cur.next
            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            if total > 9:
                cur.next = ListNode(total - 10)
                carry = 1
            else:
                cur.next = ListNode(total)
                carry = 0
            cur = cur.next
            l2 = l2.next
        
        if carry == 1:
            cur.next = ListNode(1)
        
        return dummy.next