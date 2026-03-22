from collections import deque

class list_implemantation:
    def __init__(self, list):
        self.returned_list = deque(list)
    
    def return_list(self):
        return self.returned_list
        
        
if __name__ == "__main__":
    l1 = list_implemantation([1,4,5,6])
    l2 =l1.return_list()
    print(l2)
    l2.reverse()
    
    print("{} is a reversed list".format(l2))