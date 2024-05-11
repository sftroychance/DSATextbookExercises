# In this problem, you are given a singly linked list and you need to remove every alternate node, starting with the second node. As you progress through the list, every second node should be deleted until you reach the end of the list.

from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def remove_every_second_node(arr):
    list = LinkedList().load_list(arr)

    current = list.head

    while current and current.next:
        current.next = current.next.next
        current = current.next

    return list.to_array()

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2]
list3 = [1]
list4 = [1, 2, 3, 4]
list5 = []

print(remove_every_second_node(list1)) # Expected: 1 -> 3 -> 5 -> null
print(remove_every_second_node(list2)) # Expected: 1 -> null
print(remove_every_second_node(list3)) # Expected: 1 -> null
print(remove_every_second_node(list4)) # Expected: 1 -> 3 -> null
print(remove_every_second_node(list5)) # Expected: null
