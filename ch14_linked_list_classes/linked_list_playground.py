from linked_list import LinkedList
from node import Node

my_list = LinkedList(Node('head'))
my_list.first_node.next_node = Node('some data')
my_list.first_node.next_node.next_node = Node('some other data')

print(my_list.read(2))
print(my_list.read(1))
print(my_list.read(3))

print('search \'some other data\':', my_list.search('some other data'))
print('search nonexistent data:', my_list.search('nonexistent data'))

my_list.insert(2, 'a new second node')
print('read after insert:', my_list.read(2))

print(my_list.last_value())

my_list.print_values()
my_list.reverse_list()
my_list.print_values()


