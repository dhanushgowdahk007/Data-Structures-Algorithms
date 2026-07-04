# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, the right half must be sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search(nums, target)
print(result)  # Output: 4

# Time Complexity: O(log N), where N is the length of the input array. We are halving the search space with each iteration.
# Space Complexity: O(1), as we are using a constant amount of space regardless of the input size.