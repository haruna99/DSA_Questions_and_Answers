def selection_sort(my_list):
    n = len(my_list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
            
    return my_list




print(selection_sort([4,2,6,5,1,3]))


 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

