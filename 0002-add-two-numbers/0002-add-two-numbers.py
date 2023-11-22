# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n), where n is the length of LL
        Space: O(1)

        This problem is easy, but figuring out the edge cases is a bit tricky. There are a 
        couple of edge cases: the length of the LLs are different, and if we have a carry (in between 
        the LLs or at then end, then we have to add a new node with val as carry).
        """
        dummy = ListNode()
        curr = dummy
        carry = 0

        # Keep iterating till we reach the end of both LLs and don't have any carry remaining
        while l1 or l2 or carry:
            # Check if the current node is null or not
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            # Add the two values and take the sum and the carry 
            addition = num1 + num2 + carry
            carry = addition//10
            addition = addition%10
            # Add the new sum to a new node
            curr.next = ListNode(addition)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummy.next