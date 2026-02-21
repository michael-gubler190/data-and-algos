"""
Group Anagrams - Medium

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]
Output: [["x"]]

Example 3:

Input: strs = [""]
Output: [[""]]

Constraints:

    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.
"""
from collections import defaultdict

# n = number of strings in strs
# m = max number of characters in a string
# Time Complexity: O(n * m)
# Space Complexity: O(n)
def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams_bucket = defaultdict(list)

    for s in strs:
        char_array = [0] * 26
        for c in s:
            char_array[ord(c) - ord('a')] += 1
        
        char_tuple = tuple(char_array)
        anagrams_bucket[char_tuple].append(s)

    return list(anagrams_bucket.values())


if __name__ == "__main__":
    strs1 = ["act", "pots", "tops", "cat", "stop", "hat"]
    strs2 = ["x"]
    strs3 = [""]

    print(group_anagrams(strs1))
    print(group_anagrams(strs2))
    print(group_anagrams(strs3))
