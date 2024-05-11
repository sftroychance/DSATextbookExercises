# Write a function that uses a stack to reverse a string. (For example, "abcde" would become "edcba".) You can work with our earlier implementation of the Stack class.

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            return None

    def read(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None

def reverse(string):
    result = ''
    stack = Stack()

    for letter in string:
        stack.push(letter)

    while stack.read():
        result += stack.pop()

    return result


print(reverse('abcde') == 'edcba')
