# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def reverse_between(arr, left, right):
    list = LinkedList().load_list(arr)

    dummy = Node('dummy')
    dummy.next = list.head

    prev = None
    current = dummy
    next = list.head

    position = 0

    conn = None
    tail = None

    while next:
        prev = current
        current = next
        next = next.next

        position += 1

        if left < position <= right:
            current.next = prev

        if position == left:
            conn = prev
            tail = current

        if position == right:
            tail.next = next

            if conn == dummy:
                list.head = current
            else:
                conn.next = current

    return list.to_array()

head = [1,2,3,4,5]
left = 2
right = 4
print(reverse_between(head, left, right) == [1, 4, 3, 2, 5])

head = [5]
left = 1
right = 1
print(reverse_between(head, left, right) == [5])

head = [3, 5]
left = 1
right = 2
print(reverse_between(head, left, right))
