# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        right = left = dummy = ListNode(-1)
        dummy.next = head
        count = 0
        while head:
            count += 1
            head = head.next
        x = count - k + 1
        while x != 0:
            right = right.next
            x -= 1
            
        
        while k!=0:
            left = left.next
            k-=1
        
        # print(left,right)
        left.val,right.val = right.val,left.val
        
        return dummy.next
            
        