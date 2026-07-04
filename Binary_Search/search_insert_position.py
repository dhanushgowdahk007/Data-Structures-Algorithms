# https://leetcode.com/problems/search-insert-position/

def searchInsertPosition(nums, target):
    left, right = 0, len(nums) -1

    while left <= right:
        mid = left + (right - left) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example usage:
nums = [1, 3, 5, 6]
target = 5
result = searchInsertPosition(nums, target)
print(result)  # Output: 2

# Time Complexity: O(log N), where N is the length of the input array. We are halving the search space with each iteration.
# Space Complexity: O(1), as we are using a constant amount of space regardless of the input size.