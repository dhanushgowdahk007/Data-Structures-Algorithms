# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def evalRPN(tokens):
    stack = []

    for c in tokens:
        if c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == '*':
            stack.append(stack.pop() * stack.pop())
        elif c == '/':
            a, b = stack.pop(), stack.pop()
            res = abs(b) // abs(a)
            if (a < 0) ^ (b < 0):
                res = -res
            stack.append(res)
        else:
            stack.append(int(c))
            
    return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
res = evalRPN(tokens)

print(res)

# Time Complexity: O(n) — Each token is processed exactly once, and every stack operation is O(1).
# Space Complexity: O(n) — In the worst case, the stack stores all operands before they are evaluated.