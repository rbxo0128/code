# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        tmp = head
        while tmp.next:
            tmp = tmp.next
            n += 1

        if n == 1:
            return None

        cur = head
        for i in range(n//2 - 1):
            cur = cur.next
        
        cur.next = cur.next.next
        return head