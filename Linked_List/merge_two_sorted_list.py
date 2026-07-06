# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = None
Head2 = None
    
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
Head = insert_node_at_end(Head, 2)
Head = insert_node_at_end(Head, 4)

Head2 = insert_node_at_end(Head2, 1)
Head2 = insert_node_at_end(Head2, 3)
Head2 = insert_node_at_end(Head2, 4)

display(Head)
display(Head2)
print()

def merge_two_sorted_list(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

    return dummy.next

Dummy = merge_two_sorted_list(Head, Head2)
display(Dummy)

# Time Complexity: O(n + m) — Each node from both linked lists is traversed exactly once.
# Space Complexity: O(1) — Only constant extra space is used (dummy node and pointers); no new nodes are created.