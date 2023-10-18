'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
'''
############### TIme O(nlogn)  Space: O(n) ##################
class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        
        def sort_func(arr):
            return arr[0]

        intervals = sorted(intervals, key=sort_func)
        maximum = -1
        for (start, end) in intervals:
            if start < maximum:
                return False
            maximum = end
        
        return True