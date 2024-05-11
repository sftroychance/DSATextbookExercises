# Given the starting node (head) of a singly linked list, your task is to find whether the linked list contains a loop. A loop in a linked list exists when a node can be revisited by continuously following the next pointers.

# You should return true if the linked list forms a loop (sometimes referred to as a circular list or a cyclic list) and false if it does not.

from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def has_cycle(arr, cycle_node):
    list = LinkedList().load_list(arr)

    if cycle_node >= 0:
        list.last_node().next = list.find_by_index(cycle_node)

    slow = list.head
    fast = list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True

    return False



list1 = [3, 2, 0, -4]
list2 = [1, 2]
list3 = [1]
list4 = [10, 20, 30, 40, 50, 60]
list5 = [5, 15, 25, 35, 45]

print(has_cycle(list1, 1)) # true
print(has_cycle(list2, 0)) # true
print(has_cycle(list3, -1)) # false
print(has_cycle(list4, 3)) # true
print(has_cycle(list5, -1)) # false
