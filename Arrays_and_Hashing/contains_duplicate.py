# leetcode 217 : https://leetcode.com/problems/contains-duplicate/

def containsDuplicat(nums):
    num_set = set()

    for n in nums:
        if n in num_set:
            return True
        num_set.add(n)
    return False

# Example usage:
nums = [1, 2, 3, 1]
result = containsDuplicat(nums)
print(result)  # Output: True

# Time Complexity: O(N), where N is the number of elements in the input list. We iterate through the list once, and each lookup in the set takes O(1) time on average.
# Space Complexity: O(N), where N is the number of elements in the input list.              

