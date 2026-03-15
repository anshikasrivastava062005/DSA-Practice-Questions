'''
. Problem Statement –
Capgemini in its online written test have a coding question, wherein the students are given a string
with multiple characters that are repeated consecutively. You’re supposed to reduce the size of this
string using mathematical logic given as in the example below:
Input:
aabbbbeeeeffggg
Output:
a2b4e4f2g3'''

s = input()

count = 1
result = ""

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)
