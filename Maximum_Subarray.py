"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
def Max_Subarray(nums):
    max_sub = nums[0]
    max_val = 0

    for num in nums: 
        if num < 0:
            max_val = 0
        max_val +=num
        max_sub = max(max_sub, max_val)
    return max_sub



def Max_Subarray_(nums):
    overall_maximum = float('-inf')    
    max_ending_here = 0

    for num in nums:
        if max_ending_here > 0:
            max_ending_here += num
        else:
            max_ending_here = num
        overall_maximum = max(overall_maximum, max_ending_here)
    return overall_maximum

