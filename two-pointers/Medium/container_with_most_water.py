"""
Container With Most Water - Medium

You are given an integer array heights where heights[i] represents the height of the ithith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:

Input: height = [2,2,2]
Output: 4

Constraints:

    2 <= height.length <= 1000
    0 <= height[i] <= 1000
"""


# n = number of heights in heights list
# Time Complexity: O(n)
# Space Complexity: O(1)
def container_with_most_water(heights: list[int]) -> int:
    max_volume = 0
    left, right = 0, len(heights) - 1

    while left < right:
        base = right - left
        smaller_height = min(heights[left], heights[right])

        volume = base * smaller_height
        if max_volume < volume:
            max_volume = volume
        
        if heights[left] == smaller_height:
            left += 1
        else:
            right -= 1
    
    return max_volume


if __name__ == "__main__":
    heights1 = [1, 7, 2, 5, 4, 7, 3, 6]
    heights2 = [2, 2, 2]

    print(container_with_most_water(heights1))
    print(container_with_most_water(heights2))
