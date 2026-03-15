'''
Reverse a String:-
You are given a string s, and your task is to reverse the string.
Examples:
Input:s = "GLA"
Output: "ALG"
Input: s = "for"
Output: "rof"
Input: s = "a"
Output: "a"
Input: "Capgemini"
Output: "inimegpaC"'''

s = input()

reversed_string = ""

for ch in s:
    reversed_string = ch + reversed_string

print(reversed_string)