# https://leetcode.com/problems/largest-rectangle-in-histogram/

def largest(heights):
    maxArea = 0
    stack = [] # [index, height]

    for idx, height in enumerate(heights):
        start = idx
        while stack and stack[-1][1] > height:
            stackIdx, stackH = stack.pop()
            maxArea = max(maxArea, stackH * (idx - stackIdx))
            start = stackIdx
        stack.append([start, height])

    for idx, height in stack:
        maxArea = max(maxArea, height * (len(heights) - idx))

    return maxArea

# Example usage
heights = [2,1,5,6,2,3]
maxArea = largest(heights)
print(maxArea)

# Time: O(n) — Every bar is pushed and popped at most once.
# Space: O(n) — The stack can store up to n bars in the worst case.