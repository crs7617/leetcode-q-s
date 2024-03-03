class Solution:
    def removeNthFromEnd(self, h: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = b = q = ListNode(0, h)
        while b.next:
            b = b.next
            n -= 1
            if n < 0:
                a = a.next
        
        a.next = a.next.next

        return q.next
