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

        # We are basically just mapping when curr.next or curr.random is pointing to null, then we should also map 
        # links[curr].next or links[curr].random (the new nodes we created) to null.
        links = {None: None}  
        curr = head

        while curr:
            links[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            links[curr].next = links[curr.next]
            links[curr].random = links[curr.random]
            curr = curr.next

        return links[head]