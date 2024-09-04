#search insert position

'''Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

'''
left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
'''

nums = [1,3,5,6]
nums = sorted(nums)
counter =0
target = 2
for num in nums:
    if num >= target:
        break
    counter+=1
print(counter)
