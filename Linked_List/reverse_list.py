# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = None
    
def insert_node_at_end(head, val):
    new_node = ListNode(val)
    
    if head is None:
        return new_node
    
    curr = head

    while curr.next:
        curr = curr.next

    curr.next = new_node

    return head

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))

Head = insert_node_at_end(Head, 1)
Head = insert_node_at_end(Head, 3)
Head = insert_node_at_end(Head, 4)
Head = insert_node_at_end(Head, 7)

display(Head)
print()
    
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

Head = reverse_list(Head)
display(Head)

# Time Complexity: O(n) — Each node is visited exactly once.
# Space Complexity: O(1) — Uses only three pointers (prev, curr, next), regardless of the list size.