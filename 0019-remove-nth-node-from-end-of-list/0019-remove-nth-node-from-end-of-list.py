# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time: O(n), where n is the no. of nodes in LL
        Space: O(1)
        """
        dummy = ListNode(0, head)
        # start at dummy so that we end up reaching the node before the one we want to delete,
        # and it helps us in edge cases like when there is only one node in LL
        left = dummy  
        right = dummy   # can use right = head, but then we would have to use [while right] below

        for _ in range(n):
            right = right.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next