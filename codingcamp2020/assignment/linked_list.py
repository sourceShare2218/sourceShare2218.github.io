class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: # Single Linked List (i.e. each node only has a pointer to the next node.)
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __len__(self):
        if self.head is None:
            return 0
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def append(self, newValue):
        """append new node at the end of the linkedlist"""
        # write your code here, you can delete comments (sentence starting with #) if you want

        # --- help0: to access properties of an instance ---
        # refer to __len__ method above
        # 1. if you want to access properties of the current class: self.property like self.head self.tail etc... (you can say self.method() like self.remove(3))
        # 2. for instances of other classes: instanceName.property like node1.next node1.value etc...

        # --- help1: create an instance of a class ---
        # newNode = Node(newValue) to create Node with newValue

        # --- help2: connect an node to the linked list ---
        # head -> node -> node -> tail
        # head -> node -> node -> tail -> newNode
        # head -> node -> node -> ex-tail -> tail (newNode)
        # node1.next = node2 to store a pointer to next node

        # --- help3: CAUTION ---
        # Don't foget about the case where there hasn't been any node contained in the linked list
        # i.e. head and tail points to None
        # Tips: use condition for when head and tail don't point to any nodes
    
    def contains(self, value):
        """return a boolean value that tells if the linked list contains node with the value passed to this method"""

        # --- help1: iterate through all nodes ---
        # refer __len__ method above
        
        # --- help2: return True ---
        # in while loop, if a node with the value is found, return true so that the method is terminated and save some time.

    def remove(self, value):
        """remove all nodes whose value is the argument value"""

        # --- help1: don't foget to connect nodes after removing a node ---
        # ... -> prevNode -> deleteNode -> nextNode -> ...
        # ... -> prevNode ---------------> nextNode -> ...

    def reverse(self):
        """reverse the linked list"""

        # --- help1: overview ---
        # nodeA(head) -> nodeB -> ... -> nodeN(tail)
        # nodeN(head) -> nodeN-1 -> ... -> nodeA(tail)

        # --- help2: complexity ---
        # Time: O(n)
        # Space: O(1)
        # where n is the length of the linked list
