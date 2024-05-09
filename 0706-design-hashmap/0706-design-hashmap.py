class ListNode:
    # we need to store key also as in a single array index, there can be multiple nodes chain and we need to retrieve the correct value for the key
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    """
    Time: O(n) worst case since we can have multiple values in the same array index, O(1) average time
    Space: O(n)

    Algorithm:
    The problem is not very difficult. We use an array to store the hashed keys and linked list nodes per 
    array index. If our hash function returns the same array index for multiple keys, then we have to store 
    the key and value as part of the linked list chain. 

    Note: We use a dummy node as the first node for every array index. This helps us in traversing the linked
    list without edge cases. For eg: if we want to remove the first node in an array index, it will be tedious 
    if we don't have a dummy node before it and we can then easily remove using curr.next == curr.next.next where
    curr is pointing to dummy node. 
    """
    def __init__(self):
        # Our first node per array index is a dummy node
        self.hashmap = [ListNode() for _ in range(1000)]    # 1000 is an arbitrary number

    def _hash(self, key):
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        hashed = self._hash(key)
        curr = self.hashmap[hashed]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hashed = self._hash(key)
        curr = self.hashmap[hashed]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        hashed = self._hash(key)
        curr = self.hashmap[hashed]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)