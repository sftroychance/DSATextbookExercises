# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# notes
# I have heard of the two-pointer technique for detecting a cycle
# set both pointers to the head, then increment pointer1 by 1 and pointer2 by 2 in a loop
# if the pointers are ever equal, there is a cycle
# if pointer2.next is None, there is no cycle (have reached the end of the linked list)

from node import Node
from linked_list import LinkedList

def create_linked_list(arr, pos):
    new_list = LinkedList()

    hold_node = None

    for idx, val in enumerate(arr):
        current_node = new_list.insert(idx, val)

        if idx == pos:
            hold_node = current_node

        if idx == len(arr) - 1:
            current_node.next_node = hold_node

    return new_list

def is_cyclic(arr, pos):
    my_list = create_linked_list(arr, pos)
    fast_ptr = my_list.first_node
    slow_ptr = my_list.first_node

    while fast_ptr and fast_ptr.next_node:
        fast_ptr = fast_ptr.next_node.next_node
        slow_ptr = slow_ptr.next_node

        if fast_ptr == slow_ptr:
            return True

    return False

print(is_cyclic([3, 2, 0, -4], 1))
print(is_cyclic([3, 2, 0, -4], -1))

