class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        """Check if the stack has no elements."""
        return self.top == None

    def push(self, x):
        """Add an element to the top of the stack."""
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        """Remove and return the element at the top of the stack."""
        if self.is_empty():
            return "Stack Underflow: Stack is empty."
        element = self.top.data
        self.top = self.top.next
        return element

    def peek(self):
        """Return the element at the top of the stack without removing it."""
        if self.is_empty():
            return "Stack Underflow: Stack is empty."
        return self.top.data

    def size(self):
        """Return the current number of elements in the stack."""
        return self.count

