'''
Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
'''

def find_duplicates(nums):
    my_dict = {}
    for num in nums:
        if num in my_dict:
            my_dict[num] += 1 
        else:
            my_dict[num] = 1 
    result = [key for (key,value) in my_dict.items() if value > 1 ]
    
    return result




print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

