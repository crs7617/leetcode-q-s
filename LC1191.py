# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def array_to_linked_list(array):
            if not array:
                return None
            res = ListNode(array[0])
            current = res
            for i in range(1, len(array)):
                current.next = ListNode(array[i])
                current = current.next
            return res

        array = []
        while head:
            array.append(head.val)
            head = head.next

        for i in range(len(array)):
            nums = 0
            for j in range(i, len(array)):
                nums += array[j]
                if nums == 0:
                    for ary in range(i, j + 1):
                        array[ary] = 0
                    break

        array = [x for x in array if x != 0]
        res = array_to_linked_list(array)

        return res
