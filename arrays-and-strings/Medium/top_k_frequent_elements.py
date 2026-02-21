"""
Top K Frequent Elements - Medium

Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1
Output: [7]

Constraints:

    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.
"""


# n = number of elements in nums
# Time Complexity: O(n)
# Space Complexity: O(n)
def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
    nums_frequency = dict()

    for num in nums:
        nums_frequency[num] = 1 + nums_frequency.get(num, 0)

    frequency_matrix = [[] for _ in range(len(nums) + 1)]

    for num_key in nums_frequency:
        num_frequency = nums_frequency.get(num_key, 0)
        frequency_matrix[num_frequency].append(num_key)
    
    result = []
    for i in range(len(frequency_matrix) - 1, 0, -1):
        for value in frequency_matrix[i]:
            result.append(value)

            if len(result) == k:
                return result


if __name__ == "__main__":
    nums1 = [1, 2, 2, 3, 3, 3]
    k1 = 2

    nums2 = [7, 7]
    k2 = 1

    nums3 = [2, 3, 1, 2, 4, 4, 4, 5, 5]
    k3 = 2

    print(top_k_frequent_elements(nums1, k1))
    print(top_k_frequent_elements(nums2, k2))
    print(top_k_frequent_elements(nums3, k3))

