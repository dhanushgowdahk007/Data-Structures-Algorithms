

class SinglyNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)
print()

# Traverse the list - O(n)
curr = Head 

while curr:
    print(curr)
    curr = curr.next
print()

# Display linked list - O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

display(Head)
print()

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next

    return False

searchResult = search(Head, 3)
print(searchResult)
print()

# Doubly Lined List
class DoublyNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)
    
DDHead = DoublyNode(4)
X = DoublyNode(5)
Y = DoublyNode(7)
Tail = DoublyNode(8)

DDHead.next = X
X.next = Y
Y.next = Tail

Tail.prev = Y
Y.prev = X
X.prev = DDHead

# Display - O(n)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))

display(DDHead)
print()

# Insert At beginning - O(1)
def insertAtbeginning(head, tail, val):
    newNode = DoublyNode(val, next=head)
    if head :
        head.prev = newNode
    else:
        tail = newNode
    return newNode, tail

DDHead, Tail = insertAtbeginning(DDHead, Tail, 1)
display(DDHead)
print()

# Insert At Ending - O(1)
def insertAtEnd(head, tail, val):
    newNode = DoublyNode(val, prev=tail)
    if tail:
        tail.next = newNode
    else:
        head = newNode
    return head, newNode

DDHead, Tail = insertAtEnd(DDHead, Tail, 9)
display(DDHead)