# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode(-1)
        cur = head
        prev.next = head
        dummy = prev
        while cur:
            # print(prev.val, cur.val)
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur 
                cur = cur.next
            
        return dummy.next
        