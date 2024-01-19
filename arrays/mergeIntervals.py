'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


class Solution(object):
    ############### Time: O(nlogn)  Space: O(n) ###############
    def merge(self, intervals):
        def func(arr):
            return arr[0]
        intervals = sorted(intervals, key=func)
        result = [intervals[0]]
        for val in intervals[1:]:
            if val[0] <= result[-1][1]:
                result[-1][1] = max(val[1], result[-1][1])
            else:
                result.append(val)
        return result
        