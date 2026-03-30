import os

class node:
    def __init__(self):
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
    

if __name__ == "__main__":
    ls = linked_list()
    head = ls.create()
    
    while head.next is not None:
        print(head.data)
        print(head.next)
        head = head.next