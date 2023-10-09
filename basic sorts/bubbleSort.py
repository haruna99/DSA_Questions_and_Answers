def bubble_sort(my_list):
    n = len(my_list)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

    return my_list


print(bubble_sort([4,2,6,5,1,3]))

 
 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """