# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        Time: O(n), where is the total no. of nodes present in LL
        Space: O(1)
        """
        # Find the mid-point of the LL using fast and slow pointer method
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None   # slow is pointing to the middle node which at the end will be the last node

        # Reverse the second half of the LL
        prev = None
        curr = mid
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Rearrange the links based on L0 -> Ln -> L1 -> Ln-1 -> ...
        p1 = head
        p2 = prev  # last element in the LL
        
        while p1 and p2:   # we don't need p1.val != p2.val since at the end, they both will point to the last node
            p1_next = p1.next
            p1.next = p2
            p1 = p1_next

            p2_next = p2.next
            p2.next = p1
            p2 = p2_next

        return head