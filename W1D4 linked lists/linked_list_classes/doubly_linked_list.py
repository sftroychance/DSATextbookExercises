from double_ended_node import Node

class DoublyLinkedList:

    def __init__(self, head = None, last = None):
        self.head = head
        self.last = last

    def read(self, target_index):
        current_node = self.head
        current_index = 0

        while current_index < target_index:
            current_node = current_node.next
            current_index += 1

            if not current_node:
                return None

        return current_node.val

    def search(self, target_value):
        current_node = self.head
        current_index = 0

        while True:
            if current_node.val == target_value:
                return current_index

            current_node = current_node.next

            if not current_node:
                return None

            current_index += 1

        return None

    def insert(self, target_index, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.last = new_node
            return

        if target_index == 0:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
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
            self.last = new_node

    def delete(self, target_index):
        if target_index == 0:
            self.head = self.head.next
            self.head.previous = None
            return

        current_node = self.head
        current_index = 0

        while current_index < (target_index - 1):
            current_node = current_node.next
            current_index += 1

        current_node.next = current_node.next.next

        if current_node.next:
            current_node.next.previous = current_node
        else:
            self.last = current_node

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.last = new_node
        else:
            new_node.previous = self.last
            self.last.next = new_node
            self.last = new_node

    def pop_head(self):
        popped_node = self.head
        self.head = self.head.next
        self.head.previous = None

        return popped_node

    def print_values(self):
        print('list values:')

        current_node = self.head

        while current_node:
            print(current_node.val)
            current_node = current_node.next

    def print_values_reverse(self):
        print('list values in reverse:')

        current_node = self.last

        while current_node:
            print(current_node.val)
            current_node = current_node.previous
