'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        ############# Time = O(nlogn) Space = O(n)
        heap = []
        for num in nums:
            heap.append(num)
            min_index = len(heap) - 1
            parent = (min_index-1)//2
            while min_index > 0 and heap[parent] > heap[min_index]:
                heap[min_index], heap[parent] = heap[parent], heap[min_index]
                min_index = parent
                parent = (min_index-1)//2
        
        
        while len(heap) > k:
            heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
            val = heap.pop()
            min_index = 0
            left = min_index*2+1
            right = min_index*2+2
            
            while left < len(heap) or right < len(heap):
                if left < len(heap) and right < len(heap):
                    if heap[left] <= heap[right]:
                        ind = left
                    else:
                        ind = right
                elif left < len(heap):
                    ind = left
                else:
                    ind = right


                if heap[min_index]> heap[ind]:
                    heap[min_index], heap[ind] = heap[ind], heap[min_index]
                    min_index = ind
                else:
                    break
                left = min_index*2+1
                right = min_index*2+2

        return heap[0] 


        





        


