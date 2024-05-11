# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# A
# two pointers (1-based)
# start right pointer at 1 (1st node)
# when right pointer reaches N
# - set left pointer to 0 (dummy node)
# when right pointer is at end (no left.next):
# - at left pointer set next to next.next to delete target node

from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def remove_nth_from_end(arr, n):
    list = LinkedList().load_list(arr)

    dummy = Node('dummy')
    dummy.next = list.head

    left = dummy

    right = list.head
    right_position = 1

    while right:
        right_position += 1
        right = right.next
        if right_position > n + 1:
            left = left.next

    left.next = left.next.next

    if left == dummy:
        list.head = dummy.next

    return list.to_array()

head = [1,2,3,4,5]
n = 2
print(remove_nth_from_end(head, n) == [1, 2, 3, 5])

head = [1]
n = 1
print(remove_nth_from_end(head, n) == [])

head = [1,2]
n = 1
print(remove_nth_from_end(head, n) == [1])
