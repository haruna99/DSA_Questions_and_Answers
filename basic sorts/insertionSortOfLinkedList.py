'''
Write an insertion_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the insertion sort algorithm.

The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list.

You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.



Input:

The LinkedList object containing a linked list with unsorted elements (self).



Output:

None. The method sorts the linked list in place.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insertion_sort(self):
        if self.length < 2:
            return
        dummy = Node(0)
        dummy.next = self.head
        self.head = self.head.next
        dummy.next.next = None
        
        current = self.head
        while current:
            prev = dummy
            temp = dummy.next
            new_node = Node(current.value)
            while temp:
                if current.value < temp.value:
                    
                    prev.next = new_node
                    new_node.next = temp
                    break
                prev = temp
                temp = temp.next
                if not temp:
                    prev.next = new_node
            current = current.next
            
     
            
        self.head = dummy.next
        temp = self.head
        while temp:
            self.tail = temp
            temp = temp.next
        
        
        





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

