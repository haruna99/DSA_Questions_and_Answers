'''

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 '''

class SmallestInfiniteSet:

    def __init__(self):
        # self.values = [num+1 for num in range(1000)]
        self.heap = [num+1 for num in range(10000)]


    def popSmallest(self) -> int:
        # self.values.sort(reverse=True)
        self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
        val = self.heap.pop()
        min_index = 0
        left = min_index*2+1
        right = min_index*2+2
        n = len(self.heap)
        while left < n and right < n:
            
            if self.heap[left] <= self.heap[right]:
                ind = left
            else:
                ind = right
            if self.heap[min_index]> self.heap[ind]:
                self.heap[min_index], self.heap[ind] = self.heap[ind], self.heap[min_index]
                min_index = ind
            else:
                break
            left = min_index*2+1
            right = min_index*2+2

        return val
    def addBack(self, num: int) -> None:
        if num not in self.heap:
            self.heap.append(num)
            min_index = len(self.heap) - 1
            parent = (min_index-1)//2
            while min_index > 0 and self.heap[parent] > self.heap[min_index]:
                self.heap[min_index], self.heap[parent] = self.heap[parent], self.heap[min_index]
                min_index = parent
                parent = (min_index-1)//2


        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)