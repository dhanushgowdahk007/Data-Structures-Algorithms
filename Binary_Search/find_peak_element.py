# https://leetcode.com/problems/find-peak-element/

def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage:
nums = [1, 2, 3, 1]
result = findPeakElement(nums)
print(result)  # Output: 2

# Time Complexity: O(log N), where N is the length of the input array. We are halving the search space with each iteration.
# Space Complexity: O(1), as we are using a constant amount of space regardless of the input size.