"""
Products of Array Except Self - Medium

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:

Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:

    2 <= nums.length <= 1000
    -20 <= nums[i] <= 20
"""


# n = number of elements in nums
# Time Complexity: O(n)
# Space Complexity: O(n)
def product_of_array_except_self(nums: list[int]) -> list[int]:
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    
    return result


if __name__ == "__main__":
    nums1 = [1, 2, 4, 6]
    nums2 = [-1, 0, 1, 2, 3]

    print(product_of_array_except_self(nums1))
    print(product_of_array_except_self(nums2))
