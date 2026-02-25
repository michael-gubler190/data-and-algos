"""
Valid Parentheses - Easy

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"
Output: true

Example 2:

Input: s = "([{}])"
Output: true

Example 3:

Input: s = "[(])"
Output: false

Explanation: The brackets are not closed in the correct order.

Constraints:

    1 <= s.length <= 1000
"""


# n = length of pattern
# Time Complexity: O(n)
# Space Complexity: O(n)
def valid_parentheses(pattern: str) -> bool:
    stack = []
    bracket_dict = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for bracket in pattern:
        if bracket == "[" or bracket == "{" or bracket == "(":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False

            top_bracket = stack.pop()
            if top_bracket != bracket_dict[bracket]:
                return False
    
    return len(stack) == 0


if __name__ == "__main__":
    pattern1 = "[]"
    pattern2 = "([{}])"
    pattern3 = "[(])"

    print(valid_parentheses(pattern1))
    print(valid_parentheses(pattern2))
    print(valid_parentheses(pattern3))
