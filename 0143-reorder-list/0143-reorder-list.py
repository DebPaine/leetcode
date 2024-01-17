# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        Time: O(n), where n is len(LL)
        Space: O(1)

        Revisit this as this is a confusing problem!
        """
        # 1. Find midpoint of LL
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the direction of the links in the second half of LL
        # Below is wrong and causes a cycle in LL, as we are reusing prev pointer which is mid, and we are again using it in 
        # the below while loop to reorder the second half of LL
        # prev = slow
        # curr = prev.next
        # prev.next = None
        
        curr = slow.next
        slow.next = None  # as the mid point will be the end of the reordered LL 
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Using a pointer to reorder the LL
        p1 = head
        p2 = prev
        while p1 and p2:
            p1_next = p1.next
            p1.next = p2
            p1 = p1_next

            p2_next = p2.next
            p2.next = p1
            p2 = p2_next


