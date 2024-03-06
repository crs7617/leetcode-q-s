class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        
        return False
