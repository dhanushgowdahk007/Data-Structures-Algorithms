# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left+1, right+1]  # Return 1-based indices
        elif current_sum < target:
            left += 1
        else: 
            right -= 1

        
    return []

# Example usage:
numbers = [2, 7, 11, 15]
result = twoSum(numbers, 9)
print(result)  # Output: [1, 2]

# Time Complexity: O(N), where N is the number of elements in the input list. We iterate through the list once using two pointers.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.