from collections import deque

class list_implemantation:
    def __init__(self, list):
        self.link_list = deque(list)    
        
if __name__ == "__main__":
    l1 = list_implemantation([1,4,5,6])
    print(l1.link_list)
    l1.link_list.reverse()
    print("{} is a reversed list".format(l1.link_list))