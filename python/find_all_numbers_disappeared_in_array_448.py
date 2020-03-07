#!/usr/local/bin/python3

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output_arr = []
        
        for i in range(len(nums)):
            if i+1 not in nums:
                output_arr.append(i+1)
                
        return output_arr

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]

    missing = Solution()
    print(missing.findDisappearedNumbers(nums))