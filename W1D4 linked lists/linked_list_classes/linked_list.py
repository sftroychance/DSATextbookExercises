from linked_list_classes.node import Node

class LinkedList:

    def __init__(self, head = None):
        self.head = head
        self.count = 1 if head else 0

    # load a list (array) of values into the linked list
    # replaces any existing list nodes
    def load_list(self, list):
        if not list:
            return self

        self.head = Node(list[0])
        append_to = self.head
        for i in range(1, len(list)):
            newNode = Node(list[i])
            append_to.next = newNode
            append_to = newNode

        self.count = len(list)

        return self

    def append_list(self, list):
        if not list:
            return self

        append_to = self.last_node()
        for val in list:
            newNode = Node(val)
            append_to.next = newNode
            append_to = newNode

        self.count += len(list)

        return self

    def find_by_index(self, target_index):
        current_node = self.head
        current_index = 0

        while current_index < target_index:
            current_node = current_node.next
            current_index += 1

            if not current_node:
                return None

        return current_node

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
        if target_index >= self.count:
            print('Index too large. No node inserted.')
            return

        new_node = Node(value)

        if target_index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_index = 0

        while current_index < (target_index - 1):
            print('current_index', current_index)
            current_node = current_node.next
            current_index += 1

        new_node.next = current_node.next
        current_node.next = new_node

        self.count += 1

    def delete(self, target_index):
        if target_index >= self.count:
            print('Index too large. No node deleted.')
            return

        if target_index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_index = 0

        while current_index < (target_index - 1):
            current_node = current_node.next
            current_index += 1

        current_node.next = current_node.next.next

        self.count -= 1

    def to_array(self):
        current_node = self.head
        arr = []

        while current_node:
            arr.append(current_node.val)
            current_node = current_node.next

        return arr

    def print_values(self):
        print('list values:')

        current_node = self.head

        while current_node:
            print(current_node.val)
            current_node = current_node.next

    def last_node(self):
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        return current_node

    def reverse_list(self):
        current_node = self.head
        next = self.head.next
        self.head.next = None

        while next:
            previous_node = current_node
            current_node = next
            next = current_node.next
            current_node.next = previous_node

        self.head = current_node

    def delete_duplicates(self):
        dummy = Node()
        dummy.next = self.head
        prev = dummy
        current = self.head

        delete_count = 0

        while current and current.next:
            if current.val == current.next.val:
                delete_count += 1
                while current.next and current.val == current.next.val:
                    delete_count += 1
                    current = current.next
                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        self.count -= delete_count
        self.head = dummy.next

