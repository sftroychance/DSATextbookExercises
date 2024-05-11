# Given a singly linked list and a specific value (referred to as the 'key'), your task is to determine how many times this key appears within the linked list. For instance, given a linked list like 1->2->1->2->1->3->1 and a key of 1, the expected result would be 4, as the key 1 appears four times in the list.

from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def count_key_occurrences(arr, target):
    list = LinkedList().load_list(arr)

    count = 0

    current = list.head

    while current:
        if current.val == target:
            count += 1

        current = current.next

    return count


list1 = [1, 2, 1, 2, 1, 3, 1]
list2 = [4, 4, 4, 4]
list3 = [1, 2, 3, 4, 5]
list4 = [5, 5, 1, 2, 3, 5, 5]
list5 = []
list6 = [1, 2, 3, 1, 1]

print(count_key_occurrences(list1, 1) == 4)
print(count_key_occurrences(list2, 4) == 4)
print(count_key_occurrences(list3, 1) == 1)
print(count_key_occurrences(list4, 5) == 4)
print(count_key_occurrences(list5, 1) == 0)
print(count_key_occurrences(list6, 1) == 3)
