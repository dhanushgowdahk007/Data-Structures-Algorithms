# https://leetcode.com/problems/two-sum/description/

def twoSum(num, target):
    num_map = {}

    for i, n in enumerate(num):
        complement = target - n
        if complement in num_map:
            return [num_map[complement], i]
        num_map[n] = i
    return []

# Example usage:
nums = [2, 7, 11, 15]
result = twoSum(nums, 9)
print(result)  # Output: [1, 0] (or [0, 1] depending on the order of the indices)

# Time Complexity: O(N), where N is the number of elements in the input list. We iterate through the list once, and each lookup in the hash map takes O(1) time on average.
# Space Complexity: O(N), where N is the number of elements in the input list.