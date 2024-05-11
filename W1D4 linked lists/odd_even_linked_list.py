# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def odd_even_list(arr):
    list = LinkedList().load_list(arr)

    odd = list.head
    even = list.head.next

    even_start = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_start

    return list.to_array()


arr = [1,2,3,4,5,6,7,8]
print(odd_even_list(arr))

arr = [1, 2, 3, 4]
print(odd_even_list(arr))

arr = [1,2,3,4,5]
print(odd_even_list(arr))

arr = [1, 2, 3]
print(odd_even_list(arr))
