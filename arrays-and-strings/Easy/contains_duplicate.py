"""
Contains Duplicate - Easy

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]
Output: true


Example 2:

Input: nums = [1, 2, 3, 4]
Output: false
"""

# n = number of elements in nums array
# Time Complexity: O(n)
# Space Complexity: O(n)
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 2, 1, 1, 1,]

    print(contains_duplicate(nums1))
    print(contains_duplicate(nums2))
    print(contains_duplicate(nums3))

