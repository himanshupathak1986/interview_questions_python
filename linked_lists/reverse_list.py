from collections import deque

class node:
    def __init(self):
        self.data = 0
        self.next = None
        
class linked_list:
    def __init__(self):
        pass
    
    def create(self):
        head = node()
        curr = head
        for i in range(1,6):
            node_object = node()
            node_object.data = i
            curr.next = node_object
            curr = node_object
            
        return head
    
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev