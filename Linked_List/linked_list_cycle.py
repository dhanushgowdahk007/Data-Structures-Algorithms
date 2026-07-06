# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = ListNode(3)
A = ListNode(2)
B = ListNode(0)
C = ListNode(-4)

Head.next = A
A.next = B
B.next = C
C.next = A

Head2 = ListNode(1)
X = ListNode(3)
Y = ListNode(3)
Z = ListNode(3)

Head2.next = X
X.next = Y
Y.next = Z

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

def cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False

cycle_result_Head = cycle(Head)
cycle_result_Head2 = cycle(Head2)
print(cycle_result_Head)
print(cycle_result_Head2)