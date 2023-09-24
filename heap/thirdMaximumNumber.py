'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''

####################### Min Heap - Time: O(n)  Space: O(1) ###########################
class Solution:
    def thirdMax(self, nums) -> int:
        
        if len(nums) <3:
            return max(nums)
        heap = []
        def left(ind):
            return ind*2 + 1

        def right(ind):
            return ind*2 + 2

        def parent(ind):
            return (ind - 1) // 2

        def pop_min():
            n = len(heap)
            heap[0], heap[n - 1] = heap[n-1], heap[0]
            heap.pop()
            if not heap:
                return
            ind = 0
            while True:
                left_child = left(ind)
                right_child = right(ind)
                if left_child < n-1 and right_child < n-1:
                    if heap[left_child] <= heap[right_child]:
                        min_index = left_child
                    else:
                        min_index = right_child
                elif left_child < n-1:
                    min_index = left_child
                else:
                    break
                if heap[min_index] < heap[ind]:
                    heap[min_index], heap[ind] = heap[ind], heap[min_index]
                    ind = min_index
                else:
                    break

        def add(value):
            if value in heap:
                return
            heap.append(value)
            ind = len(heap) - 1
            
            while ind > 0:
                par = parent(ind)
                if heap[par] > heap[ind]:
                    heap[par], heap[ind] = heap[ind], heap[par]
                    ind = par
                else:
                    break

        for num in nums:
            add(num)
            if len(heap) > 3:
                pop_min()
        if len(heap) <3:
            return max(heap)
        return heap[0]

############################### Three pointers - Time: O(n)  Space: O(1) ############################
class Solution1:
    def thirdMax(self, nums) -> int:
        
        maximum = float("-inf")
        second_max = float("-inf")
        third_max = float("-inf")

        for num in nums:
            new_max = max(num, maximum)
            if new_max > maximum:
                second_max, third_max = maximum, second_max
                maximum = new_max
            elif num > second_max and maximum > num:
                third_max, second_max = second_max, num
            elif num > third_max  and maximum > num  and second_max > num:
                third_max = num
            print(maximum, second_max, third_max)
        if third_max > float("-inf"):
            return third_max
        
        return maximum