# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):

    def __init__(self, nums):
        self.prefix = []
        currSum = 0

        for n in nums:
            currSum += n
            self.prefix.append(currSum)
    
    def sumRange(self, left, right):
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0

        return rightSum - leftSum
    
# Example usage:
nums = [-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)

print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))

# Time Complexity: O(n) for initialization, O(1) per sumRange() query.
# Space Complexity: O(n) for storing the prefix sum array.