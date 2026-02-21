"""
Valid Anagram - Easy

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"
Output: true

Example 2:

Input: s = "jar", t = "jam"
Output: false

Constraints:
    s and t consist of lowercase English letters.
"""



# n = number of chars in strings
# Time Complexity: O(n)
# Space Complexity: O(1)
def valid_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    char_array = [0] * 26
    for c in s1:
        char_array[ord(c) - ord('a')] += 1
    
    for c in s2:
        char_array[ord(c) - ord('a')] -= 1
    
    return char_array == [0] * 26


if __name__ == "__main__":
    str1 = "racecar"
    str2 = "carrace"

    str3 = "jar"
    str4 = "jam"

    str5 = "evil"
    str6 = "vile"

    print(valid_anagram(str1, str2))
    print(valid_anagram(str3, str4))
    print(valid_anagram(str5, str6))

