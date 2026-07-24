"""
This module provides a stack-based algorithm to check for valid parentheses.
"""

class ValidParentheses:
    """
    A class to validate parentheses combinations using a static array stack.
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

    def push(self, x: str):
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

    def is_valid_parentheses(self, expr: str):
        """Validate if the brackets in the string are matched correctly."""
        for char in expr:
            # If it's an opening bracket, push to our stack
            if char in ('{', '[', '('):
                self.push(char)
            # If it's a closing bracket, validate against the top element
            elif char in ('}', ']', ')'):
                if self.is_empty():
                    return False
                
                top_element = self.stack[self.top]
                
                # Check for mismatch before removing the element
                if char == '}' and top_element != '{':
                    return False
                if char == ')' and top_element != '(':
                    return False
                if char == ']' and top_element != '[':
                    return False
                
                # Match found, safely pop it
                self.pop()
                
        # If stack is empty at the end, all brackets matched perfectly
        return self.is_empty()
