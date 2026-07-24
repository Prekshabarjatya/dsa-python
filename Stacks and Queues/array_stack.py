"""
This module provides a static array implementation of a Stack.
"""

class ArrayStack:
    """
    A class to represent a bounded LIFO Stack using a static array.
    """
    def __init__(self, capacity: int):
        self.top = -1
        self.capacity = capacity
        # Pre-fill the array with None placeholders to allocate static space
        self.stack = [None] * capacity

    def is_empty(self):
        """Check if the stack has no elements."""
        return self.top == -1

    def is_full(self):
        """Check if the stack has reached maximum capacity."""
        return self.top == self.capacity - 1

    def push(self, x):
        """Add an element to the top of the stack."""
        if self.is_full():
            return "Stack Overflow: Stack is full."
        self.top = self.top + 1
        self.stack[self.top] = x
        return None

    def pop(self):
        """Remove and return the element at the top of the stack."""
        if self.is_empty():
            return "Stack Underflow: Stack is empty."
        element = self.stack[self.top]
        self.stack[self.top] = None  # Clean up the slot
        self.top = self.top - 1
        return element

    def peek(self):
        """Return the element at the top of the stack without removing it."""
        if self.is_empty():
            return "Stack Underflow: Stack is empty."
        return self.stack[self.top]

    def size(self):
        """Return the current number of elements in the stack."""
        return self.top + 1