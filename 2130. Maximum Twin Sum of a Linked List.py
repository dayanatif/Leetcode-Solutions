# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        head2 = prev
        maxsum = 0

        while head2:
            maxsum = max(maxsum,head.val+head2.val)
            head = head.next
            head2 = head2.next

        return maxsum
