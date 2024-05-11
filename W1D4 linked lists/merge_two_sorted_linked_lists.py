# Given two sorted singly linked lists, your task is to combine them into a single sorted linked list. The new list should be composed of the nodes from the two original lists and should also be sorted in ascending order (where node values are equal to or increase as you move through the linked list).

from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def merge_sorted_lists(arr1, arr2):
    list1 = LinkedList().load_list(arr1)
    list2 = LinkedList().load_list(arr2)

    list1_current = list1.head
    list2_current = list2.head

    dummy = Node('dummy')
    current = dummy

    while list1_current and list2_current:
        if list1_current.val < list2_current.val:
            current.next = list1_current
            list1_current = list1_current.next
        else:
            current.next = list2_current
            list2_current = list2_current.next

        current = current.next

    current.next = list1_current if list1_current else list2_current

    outlist = LinkedList(dummy.next)

    return outlist.to_array()



list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2)) # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null

list3 = [1, 2, 3]
list4 = []
print(merge_sorted_lists(list3, list4)) # Expected: 1 -> 2 -> 3 -> null

list5 = []
list6 = [1]
print(merge_sorted_lists(list5, list6)) # Expected: 1 -> null

list7 = [1, 5, 9]
list8 = [2, 4, 6, 8, 10]
print(merge_sorted_lists(list7, list8)) # Expected: 1 -> 2 -> 4 -> 5 -> 6 -> 8 -> 9 -> 10 -> null

list9 = [1, 2, 5]
list10 = [3, 6, 7]
print(merge_sorted_lists(list9, list10)) # Expected: 1 -> 2 -> 3 -> 5 -> 6 -> 7 -> null
