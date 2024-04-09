from double_ended_node import Node

class DoublyLinkedList:

    def __init__(self, first_node = None, last_node = None):
        self.first_node = first_node
        self.last_node = last_node

    def read(self, target_index):
        current_node = self.first_node
        current_index = 0

        while current_index < target_index:
            current_node = current_node.next_node
            current_index += 1

            if not current_node:
                return None

        return current_node.data

    def search(self, target_value):
        current_node = self.first_node
        current_index = 0

        while True:
            if current_node.data == target_value:
                return current_index

            current_node = current_node.next_node

            if not current_node:
                return None

            current_index += 1

        return None

    def insert(self, target_index, value):
        new_node = Node(value)

        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
            return

        if target_index == 0:
            self.first_node.previous_node = new_node
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        current_node = self.first_node
        current_index = 0

        while current_index < (target_index - 1):
            current_node = current_node.next_node
            current_index += 1

        new_node.previous_node = current_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

        if new_node.next_node:
            new_node.next_node.previous_node = new_node
        else:
            self.last_node = new_node

    def delete(self, target_index):
        if target_index == 0:
            self.first_node = self.first_node.next_node
            self.first_node.previous_node = None
            return

        current_node = self.first_node
        current_index = 0

        while current_index < (target_index - 1):
            current_node = current_node.next_node
            current_index += 1

        current_node.next_node = current_node.next_node.next_node

        if current_node.next_node:
            current_node.next_node.previous_node = current_node
        else:
            self.last_node = current_node

    def append(self, value):
        new_node = Node(value)

        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def pop_head(self):
        popped_node = self.first_node
        self.first_node = self.first_node.next_node
        self.first_node.previous_node = None

        return popped_node


    def print_values(self):
        print('list values:')

        current_node = self.first_node

        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def print_values_reverse(self):
        print('list values in reverse:')

        current_node = self.last_node

        while current_node:
            print(current_node.data)
            current_node = current_node.previous_node
