from double_ended_node import Node
from linked_list import LinkedList

class DoublyLinkedList(LinkedList):

    def __init__(self, first_node = None, last_node = None):
        super().__init__(first_node)
        self.last_node = last_node

    def insert(self, target_index, value):
        new_node = Node(value)

        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
            return

        if target_index == 0:
            self.first_node.previous = new_node
            new_node.next = self.first_node
            self.first_node = new_node
            return

        current_node = self.first_node
        current_index = 0

        while current_index < (target_index - 1):
            current_node = current_node.next
            current_index += 1

        new_node.previous = current_node
        new_node.next = current_node.next
        current_node.next = new_node

        if new_node.next:
            new_node.next.previous = new_node
        else:
            self.last_node = new_node

    def delete(self, target_index):
        if target_index == 0:
            self.first_node = self.first_node.next
            self.first_node.previous = None
            return

        current_node = self.first_node
        current_index = 0

        while current_index < (target_index - 1):
            current_node = current_node.next
            current_index += 1

        current_node.next = current_node.next.next

        if current_node.next:
            current_node.next.previous = current_node
        else:
            self.last_node = current_node

    def append(self, value):
        new_node = Node(value)

        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous = self.last_node
            self.last_node.next = new_node
            self.last_node = new_node

    def pop_head(self):
        popped_node = self.first_node
        self.first_node = self.first_node.next
        self.first_node.previous = None

        return popped_node

    def print_values_reverse(self):
        print('list values in reverse:')

        current_node = self.last_node

        while current_node:
            print(current_node.val)
            current_node = current_node.previous

    def last_value(self):
        return self.last_node.val
