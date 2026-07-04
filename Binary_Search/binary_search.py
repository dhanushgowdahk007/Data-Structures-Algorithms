# https://leetcode.com/problems/binary-search/

def binarySearch(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + ((right-left)// 2)

        if target == nums[mid]:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1

    return -1

# Example usage:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = binarySearch(nums, target)
print(result)  # Output: 4

# Time Complexity: O(log N), where N is the length of the input array. We are halving the search space with each iteration.
# Space Complexity: O(1), as we are using a constant amount of space regardless of