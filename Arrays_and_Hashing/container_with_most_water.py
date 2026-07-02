# https://leetcode.com/problems/container-with-most-water

def maaxArea(height):

    res = 0

    # for l in range(len(height)):
    #     for r in range(l+1, len(height)):
    #         area = (r-l) * min(height[l], height[r])
    #         res = max(res, area)

    left, right = 0, len(height)-1

    while left < right:
        area = (right-left) * min(height[left], height[right])
        res = max(res, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return res

# Example usage:
height = [1,8,6,2,5,4,8,3,7]
result = maaxArea(height)
print(result)  # Output: 49

# Time Complexity: O(N^2), where N is the number of elements in the input list. We have a nested loop that iterates through all pairs of lines.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.