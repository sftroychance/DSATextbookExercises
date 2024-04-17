# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# A
# Create linked lists out of the given arrays
# set primary list to list with smallest first value; other list to other list
# next_other = other.first_node
# current_node = primary.first_node
# while next_other and current_node:
#   if next_other.value <= current_node.next_node.value
#       next_next = next_other.next_node
#       next_current = current_node.next_node
#       current_node.next = next_other
#       next_other.next_node = next_current
#       next_other = next_next
#       current_node = current_node.next
#   else:
#       current_node = current_node.next

# Big O values assume linked lists are already created before merging
# Time: O(N + M)
# Space: O(1)

# revision: try to take advantage of the insert method for the linked list
#   would need to keep track of index while iterating primary list
# => it would actually complicate this function more

from node import Node
from linked_list import LinkedList

def create_linked_list(arr):
    new_list = LinkedList()

    for idx, val in enumerate(arr):
        new_list.insert(idx, val)

    return new_list

def merge_lists(arr1, arr2):
    list1 = create_linked_list(arr1)
    list2 = create_linked_list(arr2)

    if not list1.first_node:
        return list2
    elif not list2.first_node:
        return list1

    if list1.first_node.data < list2.first_node.data:
        primary = list1
        other = list2
    else:
        primary = list2
        other = list1

    current_node = primary.first_node
    next_other = other.first_node

    while current_node and next_other:
        if not current_node.next_node:
            current_node.next_node = next_other
            return primary

        if next_other.data <= current_node.next_node.data:
            # save next node in other list
            next_next = next_other.next_node
            # save next node in current list
            next_current = current_node.next_node

            # insert other node into current list
            current_node.next_node = next_other
            next_other.next_node = next_current

            next_other = next_next

        current_node = current_node.next_node

    return primary

print('#1')
merge_lists([1, 2, 2, 4], [1, 3, 4]).print_values()
print('#2')
merge_lists([], [1, 3, 4]).print_values()
print('#3')
merge_lists([1, 2, 2, 4], [1, 3, 4, 8, 9, 10, 12]).print_values()
print('#4')
merge_lists([2], [1]).print_values()
print('#5')
merge_lists([1, 2, 2, 4], [1]).print_values()
