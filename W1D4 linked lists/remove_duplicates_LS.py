# Given the head of a sorted singly linked list, eliminate any duplicate elements, ensuring each value in the list is unique. The resulting linked list must remain sorted. Modify the linked list and return the head of the revised, duplicate-free list.

from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def delete_duplicates(arr):
    list = LinkedList().load_list(arr)

    current = list.head

    while current and current.next:
        while current.next and current.val == current.next.val:
            current.next = current.next.next

        current = current.next

    return list.to_array()

list1 = [1, 1, 2]
list2 = [1, 1, 2, 3, 3]
list3 = [1, 2, 3, 3, 4]
list4 = [2, 2, 2, 3, 3]
list5 = [5]

print(delete_duplicates(list1)) # Expected: "1 -> 2 -> null"
print(delete_duplicates(list2)) # Expected: "1 -> 2 -> 3 -> null"
print(delete_duplicates(list3)) # Expected: "1 -> 2 -> 3 -> 4 -> null"
print(delete_duplicates(list4)) # Expected: "2 -> 3 -> null"
print(delete_duplicates(list5)) # Expected: "5 -> null"
