"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time: O(n), where n is the length of LL
        Space: O(n), since we are using a hashmap

        We are using a two-pass strategy. First pass is to store all the nodes as copy
        in our hashmap. Second pass is to link the next and random pointers to the nodes.
        We basically store the curr and new node mapping in our hashmap so that in the second
        pass we can rebuild all the next and random links.
        """
        hashmap = {None: None}  # for cases where curr.next or curr.random is pointing to null
        curr = head

        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            hashmap[curr].next = hashmap[curr.next]
            hashmap[curr].random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]