from linked_list import LinkedList
from node import Node

my_list = LinkedList(Node('one'))
my_list.insert(1, 'two')
my_list.insert(2, 'three')
my_list.insert(3, 'four')
my_list.insert(4, 'five')

my_list.print_values()

node2 = my_list.first_node.next_node.next_node
node3 = node2.next_node

# to delete node2 without knowing about the list
node2.data = node3.data
node2.next_node = node3.next_node

my_list.print_values()
