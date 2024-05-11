# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# A:
# create linked list from given array
# set current node to head
# loop while current_node and current_node.next
#   iterate over next nodes until reaching a value not equal to value of current node
#   set current node.next to that node
#   set current node to current_node.next


from node import Node
from linked_list import LinkedList

def create_linked_list(arr):
    new_list = LinkedList()

    for idx, val in enumerate(arr):
        new_list.insert(idx, val)

    return new_list

def remove_duplicates(arr):
    my_list = create_linked_list(arr)

    current_node = my_list.first_node

    while current_node and current_node.next_node:
        next = current_node.next_node
        while next and current_node.data == next.data:
            next = next.next_node
        current_node.next_node = next
        current_node = next

    return my_list

remove_duplicates([1, 1, 2]).print_values()
remove_duplicates([0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5]).print_values()
