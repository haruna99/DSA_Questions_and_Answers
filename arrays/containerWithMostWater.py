'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height)-1
        max_height = 0
        while left <right:
            new_max_height = (right-left)*min(height[left], height[right])
            max_height = max(max_height, new_max_height)
            if height[left] <= height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
        return max_height