# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative solution 
        """
        Time: O(n), where n is the total no. of nodes present in LL
        Space: O(1)
        """
        # curr = head
        # prev = None

        # while curr:
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_node

        # return prev


        # Recursive solution (try out visually, much easier to understand)
        """
        Time: O(n)
        Space: O(n), since we are using the call stack for recursion
        """
        if not head:   # for scenario where user enters empty or null linked list
            return None
        if not head.next:   # for scenario where we reach the end of a linked list
            return head

        new_head = self.reverseList(head.next)   # reach the end of the linked list and get the new head
        head.next.next = head   # if head is 4, head.next = 5, 5.next should point back to 4 so that it's reversed
        head.next = None   # now head is 4, so it's pointing to 5 and 5 is pointing back to 4, and 3 is pointing to 4 too, so we get rid of 4.next
        """
        We return the new head which is 5 (the last node) in every recursive call since we want to pass the new head 
        from the top of the call stack (when we reach the last node) till the bottom of the 
        stack (when we reach the first node) so that we can get the starting node of this reversed linked list
        """ 
        return new_head   