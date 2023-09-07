'''
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

 

Example 1:

Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.
Example 2:

Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.
'''

############ Time: O((k+candidates)log(candidates))  Space: O(candidates) ####################
class Solution:
    def __init__(self):
        self.heap1 = []
        self.heap2 = []
    def addToHeap(self, heap, value):
        heap.append(value)
        min_index = len(heap) - 1
        while min_index > 0:
            parent = self.getParent(min_index)
            if heap[parent] > heap[min_index]:
                heap[parent], heap[min_index] = heap[min_index], heap[parent]
                min_index = parent
            else:
                break

    def remove(self, heap):
        n = len(heap)
        if n == 1:
            return heap.pop()
        heap[0], heap[n-1] = heap[n-1], heap[0]
        result = heap.pop()
        min_index = 0
        left = self.getLeft(min_index)
        right = self.getRight(min_index)
        while left < len(heap) or right < len(heap):
            if left < len(heap) and right < len(heap):
                if heap[left] <= heap[right]:
                    ind = left
                else:
                    ind = right
            elif left < len(heap):
                ind = left

            if heap[ind] < heap[min_index]:
                heap[ind], heap[min_index] = heap[min_index], heap[ind]
                min_index = ind
            else:
                break
            left = self.getLeft(min_index)
            right = self.getRight(min_index)
            

    def getParent(self, index):
        return (index-1)//2

    def getLeft(self, index):
        return index*2 + 1

    def getRight(self, index):
        return index*2 + 2

    def totalCost(self, costs, k: int, candidates: int) -> int:
        
        total = 0
        n1 = len(costs)
        for i in range(candidates):
            if n1 %2 != 0:
                if i == (n1+1)/2 -1:
                    self.addToHeap(self.heap1, costs[i])
                    break
            self.addToHeap(self.heap1, costs[i])
            self.addToHeap(self.heap2, costs[-i-1])
            if n1 % 2 == 0:
                if i == n1/2-1:
                    break
        heap1_n = len(self.heap1)
        heap2_n = len(self.heap2)
        
        for i in range(k):
            if self.heap1 and self.heap2:
                val1 = self.heap1[0]
                val2 = self.heap2[0]
            
                if val1 <= val2:
                    
                    total += val1
                    
                    self.remove(self.heap1)
                    if heap1_n + heap2_n < len(costs):
                        self.addToHeap(self.heap1, costs[heap1_n])
                    heap1_n += 1
                else:
                    total += val2
                    
                    self.remove(self.heap2)
                    if heap1_n + heap2_n < len(costs):
                        self.addToHeap(self.heap2, costs[-heap2_n-1])
                    heap2_n += 1
            elif self.heap1:
                total += self.heap1[0]
                self.remove(self.heap1)
                if heap1_n + heap2_n < len(costs):
                    self.addToHeap(self.heap1, costs[heap1_n])
                heap1_n += 1
            elif self.heap2:
                total += self.heap2[0]
                self.remove(self.heap2)
                if heap1_n + heap2_n < len(costs):
                    self.addToHeap(self.heap2, costs[-heap2_n-1])
                heap2_n += 1
            

        return total
            
