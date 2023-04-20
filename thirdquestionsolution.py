class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getMiddle(head):
    slow_ptr = head
    fast_ptr = head

    # Traverse the list using two pointers: slow_ptr and fast_ptr
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Return the data at the middle node of the linked list
    return slow_ptr.data
