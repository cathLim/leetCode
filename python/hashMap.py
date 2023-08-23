https://leetcode.com/problems/design-hashmap/
"""
In this case, we would like to solve the problem
by creating a hashmap which has the maximum operation of 1000 times

Concern: Hashmap collision
There are many ways to handle for it
e.g.
1. Open Addressing
2. Chaining 
... etc

We will go for the chaining method, using the linked-list
and creates a dummy nodes infront of the first node

"""
class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key):
        return key % len(self.map)
    
    def put(self, key: int, value: int) -> None:
        #this is a dummy node
        current = self.map[self.hash(key)]
        while current.next:
            #which means the key is found
            if current.next.key == key:
                current.next.val = value
                return
            current = current.next
        current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        #to get the val, we no need to start from dummy node
        #start from the first node
        current = self.map[self.hash(key)].next
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        #have to start from the dummy node
        #to avoid accidentally remove the first node
        current = self.map[self.hash(key)]
        #check is dummy and first node empty
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)