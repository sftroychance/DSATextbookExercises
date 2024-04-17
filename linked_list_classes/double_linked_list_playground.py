from double_ended_node import Node
from doubly_linked_list_inherited import DoublyLinkedList

my_list = DoublyLinkedList()
my_list.insert(0, 'zero')
my_list.insert(1, 'one')
my_list.insert(2, 'two')
my_list.insert(3, 'three')

my_list.print_values()

my_list.delete(3)
my_list.delete(0)
my_list.insert(1, 'between zero and one')

my_list.print_values()
my_list.print_values_reverse()

my_list.append(24)
my_list.print_values()
print('popped first value:', my_list.pop_head().data)
my_list.print_values()

print(my_list.read(2))
