'''
Palindrome String:-
Given a string s, the task is to check if it is palindrome or not.
Example:
Input: s = "abba"
Output: true
Input: s = "abc"
Output: flase
Input: "madam"
Output: true'''

s = input()

if s == s[::-1]:
    print("true")
else:
    print("false")