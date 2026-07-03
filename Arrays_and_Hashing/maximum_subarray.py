# https://leetcode.com/problems/maximum-subarray/

def maxSubarray(nums):
    maxSum = nums[0]
    currentSum = 0

    for num in nums:
        if currentSum < 0:
            currentSum = 0

        currentSum += num
        maxSum = max(maxSum, currentSum)

    return maxSum

# Example usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSubarray(nums)
print(result)  # Output: 6
# Time Complexity: O(N), where N is the number of elements in the input list. We iterate through the list once.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless