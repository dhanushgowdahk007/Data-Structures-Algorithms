# https://leetcode.com/problems/min-stack/

class Stack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]
    
    def __str__(self):
        return str(self.stack)

stk = Stack()
stk.push(3)
stk.push(5)
stk.push(2)
stk.push(4)

print(stk)
print()
stk.pop()
stk.push(9)
print(stk)
print()
print(stk.top())
print()
print(stk.getMin())

# push() → O(1)
# pop() → O(1)
# top() → O(1)
# getMin() → O(1)
# Space: O(n) (an auxiliary stack stores the minimum value at each depth).