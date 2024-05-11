from linked_list_classes.node import Node
from linked_list_classes.linked_list import LinkedList

def delete_duplicates(arr):
    list = LinkedList().load_list(arr)

    dummy = Node('dummy')
    dummy.next = list.head
    prev = dummy
    current = list.head

    while current and current.next:
        if current.val == current.next.val:
            while current.next and current.val == current.next.val:
                current = current.next
            prev.next = current.next
        else:
            prev = prev.next

        current = current.next

    list.head = dummy.next
    return list.to_array()

arr = [1,2,3,3,4,4,5]
print(delete_duplicates(arr))# == [1, 2, 5])

arr = [1, 1, 1, 2, 3]
print(delete_duplicates(arr))# == [2, 3])
