"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""

from tkinter import S
from typing import Counter

#solution1
def validAnagram(s, t):
    return sorted(s) == sorted(t)


#solution2
def validAnagram1(s, t):
    if len(s) != len(t):
        return False
    dict1, dict2 = {}, {}
    for i in range(len(s)):
        dict1[s[i]] = 1 + dict1.get(s[i], 0)
        dict2[t[i]] = 1+ dict2.get(t[i], 0)
    for c in dict1:
        if dict1[c] != dict1.get(c, 0):
            return False

#solution3
def validAnagram2(s, t):
    return Counter(s) == Counter(t)

#~~~~~~~Testing~~~~~~~~~~

s = "anagram"
t = "nagaram"

print(validAnagram(s, t))