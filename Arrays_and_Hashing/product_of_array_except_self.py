# https://leetcode.com/problems/product-of-array-except-self

def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n

    # Calculate the left products
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]

    # Calculate the right products and multiply with the left products
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output   

# Example usage:
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]

# Time Complexity: O(N), where N is the number of elements in the input list. We iterate through the list twice, once for the left products and once for the right products.
# Space Complexity: O(1) (excluding the output array), as we are using a constant amount of extra space for the left and right products. The output array is not counted towards the space complexity since it is required for the result.