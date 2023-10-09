'''
Write a selection_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the selection sort algorithm. The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list. You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.



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

    def selection_sort(self):
        if self.length <= 1:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        
        start = dummy
        
        while start.next:
            temp = start
            minimum = start
            while temp.next:
                if temp.next.value < minimum.next.value:
                    minimum = temp
                temp = temp.next
                
            if minimum != start:
                if start.next == minimum:
                    start.next = minimum.next
                    minimum.next = minimum.next.next
                    start.next.next = minimum
                else:
                    cur1 = start.next
                    after1 = cur1.next
                    cur2 = minimum.next
                    after2 = cur2.next
                    
                    start.next = cur2
                    minimum.next = cur1
                    cur2.next = after1
                    cur1.next = after2
                    
            start = start.next
        
        self.head = dummy.next
            



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

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

