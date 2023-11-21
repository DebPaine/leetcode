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
        """
        copy = { None: None }  # for cases where curr.next or curr.random is pointing to null
        curr = head

        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            current_node = copy[curr]
            current_node.next = copy[curr.next]
            current_node.random = copy[curr.random]
            curr = curr.next
        
        return copy[head]