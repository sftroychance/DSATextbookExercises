# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def add_two_numbers(l1, l2):
    l1_ptr = LinkedList().load_list(l1).head
    l2_ptr = LinkedList().load_list(l2).head

    out = LinkedList(Node(0))

    output = out.head
    running_sum = output
    carry = 0

    while l1_ptr and l2_ptr:
        sum = l1_ptr.val + l2_ptr.val + carry
        running_sum.val = sum % 10
        carry = sum // 10

        l1_ptr = l1_ptr.next
        l2_ptr = l2_ptr.next

        if l1_ptr or l2_ptr:
            running_sum.next = Node()
            running_sum = running_sum.next

    remaining = l1_ptr if l1_ptr else l2_ptr

    while remaining:
        sum = remaining.val + carry
        running_sum.val = sum % 10
        carry = sum // 10

        remaining = remaining.next
        if remaining:
            running_sum.next = Node()
            running_sum = running_sum.next

    if carry:
        running_sum.next = Node(carry)

    return out.to_array()


l1 = [2,4,3]
l2 = [5,6,4]
Output = [7,0,8]
print(add_two_numbers(l1, l2) == Output)

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
Output = [8,9,9,9,0,0,0,1]
print(add_two_numbers(l1, l2) == Output)
