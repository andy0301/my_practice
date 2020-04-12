#!/usr/bin/env python

"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # check if len(intervals) <= 1, that means 0 or 1 interval there
        # so just return it
        if len(intervals) <= 1:
            return intervals
        
        # define output_arr
        output_arr = []
        
        # sort intervals for easy search
        intervals.sort()
        
        # init current_interval
        # intervals = [[1,3],[2,6],[8,10],[15,18]]
        # eg: current_interval = intervals[0] = [1,3]
        current_interval = intervals[0]
        output_arr.append(current_interval)
        
        # loop intervals to get which array need merge
        # compare the last element from current interval 
        # with first element from next interval
        for i in range(1,len(intervals)):
            current_begin = current_interval[0]
            current_end = current_interval[1]
            next_interval = intervals[i]
            next_begin = next_interval[0]
            next_end = next_interval[1]
            
            if (current_end >= next_begin):
                current_interval[1] = max(current_end, next_end)
            else:
                current_interval = next_interval
                output_arr.append(current_interval)
        
        return output_arr
            
            
            
            
            
            