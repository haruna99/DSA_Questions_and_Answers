'''
Write a function item_in_common(list1, list2) that takes 
two lists as input and returns True if there is at least one 
common item between the two lists, False otherwise.
'''

def item_in_common(l1,l2):
    my_dict = {key:True for key in l1}
    
    for value in l2:
        if value in my_dict:
            return True
    return False



list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))