# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        op = ''
        pointer = head
        while pointer:
            op += str(pointer.val)
            pointer = pointer.next
        
        return op == op[::-1]
        