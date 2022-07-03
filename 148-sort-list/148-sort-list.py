# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        ls = []
        while pointer:
            ls.append(pointer.val)
            pointer = pointer.next
        
        ls.sort()
        dummy = curr = ListNode(0)
        
        for num in ls:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next
            