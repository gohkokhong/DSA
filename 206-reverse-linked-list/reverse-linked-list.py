# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, curr, next
        prev, current = None, head

        # While curr is not null
        while current:
            tempNext = current.next

            # Reversal next > prev
            current.next = prev

            prev = current

            current = tempNext

        # Return new head
        return prev