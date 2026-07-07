# https://leetcode.com/problems/valid-parentheses/

def valid_praenthese(s):
    stack = []
    closeToOpen = { ')' : '(', '}': '{', ']' : '['}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False

# Example usage:
s = "()[]{}"
res = valid_praenthese(s)

print(res)

# Time Complexity: O(n) — Each character is processed exactly once, with every push and pop taking O(1).
# Space Complexity: O(n) — In the worst case (e.g., "((({"), the stack stores all opening brackets.