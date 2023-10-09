def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1, n):
        j = i-1
        ind = i
        while my_list[ind]<my_list[j] and ind >= 0 and j >= 0:
            my_list[ind], my_list[j] = my_list[j], my_list[ind]
            ind -= 1
            j -= 1
            
    return my_list




print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

