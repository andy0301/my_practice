#!/usr/local/bin/python3
"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output_arr = []

        if len(nums) <= 1:
            return output_arr
        
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                output_arr.append(nums[i])

        return set(output_arr)

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]

    output = Solution()
    print(output.findDuplicates(nums))