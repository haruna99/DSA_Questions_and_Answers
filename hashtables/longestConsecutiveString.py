'''
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.
'''


def longest_consecutive_sequence(nums):
    nums.sort()
    my_set = set()
    length = 0
    max_length = 0
    for i in range(len(nums)):
        diff = nums[i]-1
        if nums[i] in my_set:
            continue
        if diff in my_set:
            length += 1
            max_length = max(max_length, length)
        else:
            length = 1
            max_length = max(max_length, length)
        my_set.add(nums[i])

    return max_length

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2,2,2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""