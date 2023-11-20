# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(min(m, n)), where m is len(list1) and n is len(list2)
        Space: O(1)
        """
        head = ListNode()
        ptr3 = head
        ptr1, ptr2 = list1, list2

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ptr3.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr3.next = ptr2
                ptr2 = ptr2.next
            ptr3 = ptr3.next

        ptr3.next = ptr1 or ptr2

        return head.next