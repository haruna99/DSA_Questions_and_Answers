def remove_duplicates(nums):
    n = len(nums)
    if n == 0:
        return 0
        
    index = 1
    for i in range(1,n):
        if nums[i] != nums[i-1]:
            nums[index] = nums[i]
            index += 1
     
    return index
    # n = len(nums)
    # i = 0
    # index = 0
    
    # while i < n:
    #     if i == n-1 and n >= 2:
    #         if nums[i] != nums[i-1]:
    #             nums[index] = nums[i]
    #     j = i+1
    #     while j < n:
    #         if nums[i] != nums[j]:
    #             nums[index] = nums[i]
    #             index += 1
    #             i = j 
    #             break
    #         else:
    #             result -= 1
    #         j += 1
    #     i = j
     
    # return result
    
    

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])


"""
    EXPECTED OUTPUT:
    ----------------
    New length: 5
    Unique values in list: [0, 1, 2, 3, 4]

"""