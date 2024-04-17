from doubly_linked_list import DoublyLinkedList

class Queue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        popped = self.data.pop_head()
        return popped.data

    def read(self):
        if not self.data.first_node:
            return None
        else:
            return self.data.first_node.data

    def print(self):
        self.data.print_values()

