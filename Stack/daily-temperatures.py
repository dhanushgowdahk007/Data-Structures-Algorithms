# https://leetcode.com/problems/daily-temperatures/

def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = [] # [temp, index]

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stackTemp, stackIdx = stack.pop()
            result[stackIdx] = (i - stackIdx)
        stack.append([temp, i])

    return result
    
temperatures = [73,74,75,71,69,72,76,73]

res = daily_temperatures(temperatures)
print(res)

# Time: O(n) — Each index is pushed and popped at most once.
# Space: O(n) — The stack may contain up to n indices in the worst case (strictly decreasing temperatures).