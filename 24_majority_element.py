'''
Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the
majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

# Approach 1

nums = list(map(int, input().split()))

n = len(nums)

for num in nums:
    if nums.count(num) > n // 2:
        print(num)
        break

# Approach 2

nums = list(map(int, input().split()))

candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)