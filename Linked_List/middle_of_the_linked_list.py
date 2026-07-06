# https://leetcode.com/problems/middle-of-the-linked-list/

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
Head = insert_node_at_end(Head, 9)

display(Head)
print()

def middle_of_the_linked_list(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

mid = middle_of_the_linked_list(Head)

display(mid)

# Time Complexity : O(n)
# Space Complexity : O(1)