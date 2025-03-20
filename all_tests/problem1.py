# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
        
    def print_linked_list(self):
        if not self.head:
            print("No element in linked List")
        
        current = self.head
        while current:
            print(current.val)
            current = current.next
            
    
    def adding_element_at_index(self, val, ind):
        if ind > self.length:
            print("index should be less than equal ", self.length)
            return
        
        node = Node(val)
        current = self.head
        
        if ind == 0:
            if current and current.val:
                print(val, ind, current)
                node.next = current
                self.head = node
            else:
                current = node
                self.head = current
        else:
            for i in range(ind-1):
                current = current.next
            
            next_node = current.next
            curr_node = current
            curr_node.next = node
            if next_node:
                node.next = next_node
                
        self.length += 1 
        
    def reverse_linked_list(self):
        curr = self.head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
        
1,23,4,5,7,8,8,9,7
k = 4


link_list = LinkedList()
link_list.adding_element_at_index(1, 1)

link_list.adding_element_at_index(1, 0)
link_list.print_linked_list()
link_list.adding_element_at_index(2, 1)
link_list.adding_element_at_index(3, 2)
link_list.adding_element_at_index(5, 2)
link_list.adding_element_at_index(6, 2)
link_list.adding_element_at_index(7, 2)

link_list.adding_element_at_index(3, 7)
link_list.adding_element_at_index(10, 0)


link_list.print_linked_list()


            