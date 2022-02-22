"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""

def isValid(s):
    stack =[]
    matching_p = {')':'(', ']':'[', '}': '{'}
    for sy in s:
        if sy in matching_p:
            if stack and stack[-1] == matching_p[sy]:
                stack.pop()
            else: 
                return False
    return True if not stack else False
