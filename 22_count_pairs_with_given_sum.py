'''
. Count pairs with given sum:-
Given an array arr[] of n integers and a target value, find the number of pairs of integers in the array
whose sum is equal to target.
Examples:
Example:-1
Input: arr[] = [1, 5, 7, -1, 5], target = 6
Output: 3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).
Example:-2
Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) and (1, 1).
Example:-3
Input: arr[] = [10, 12, 10, 15, -1], target = 125
Output: 0
Explanation: There is no pair with sum = target
'''

arr = list(map(int, input().split()))
target = int(input())

count = 0
n = len(arr)

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            count += 1

print(count)