'''
Binary Search:
Implement a binary search algorithm to find a target value in a sorted array.
Input: Array: [1, 2, 3, 4, 5, 6, 7, 8, 9], Target: 4
Output: 3
Explanation: The function returns the index of the target value in the array
'''

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1,2,3,4,5,6,7,8,9]
target = 4

result = binary_search(arr, target)
print(result)
