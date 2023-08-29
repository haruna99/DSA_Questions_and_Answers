'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)
        result = []

        i = j = 0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                result.append(nums2[j])
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                result.append(nums2[j])
                j += 1

        if i<n:
            for num in nums1[i:]:
                result.append(num)

        if j<m:
            for num in nums2[j:]:
                result.append(num)

        print(result)

        n = len(result)

        if n%2 == 0:
            output = (result[int(n/2)-1] + result[int(n/2)])/2
        else:
            output = result[int((n+1)/2)-1]

        return output

