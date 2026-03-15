'''
 String Rotation Check:-
Given two strings s and goal, return true if and only if s can become goal after some number of shifts
on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:
Input: s = "abcde", goal = "abced"
Output: false
'''

s = input()
goal = input()

if len(s) != len(goal):
    print(False)

elif goal in (s + s):
    print(True)

else:
    print(False)