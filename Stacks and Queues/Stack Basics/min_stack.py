"""
This module provides a static array implementation of a Min Stack.
All operations achieve strict O(1) time complexity.
"""

class MinStack:
    """
    A class to represent a bounded LIFO Stack using static arrays.
    It tracks and retrieves the minimum element in O(1) time complexity.
    """
    def __init__(self, capacity: int):
        self.top = -1
        self.capacity = capacity
        # Main array to store standard inserted elements
        self.stack = [None] * capacity
        # Companion array to map the historical minimum value at each index depth
        self.min_stack = [None] * capacity

    def is_empty(self) -> bool:
        """Check if the stack has no elements. Time Complexity: O(1)"""
        return self.top == -1

    def is_full(self) -> bool:
        """Check if the stack has reached maximum capacity. Time Complexity: O(1)"""
        return self.top == self.capacity - 1

    def push(self, x: int):
        """Add an element and update minimum tracking. Time Complexity: O(1)"""
        if self.is_full():
            return "Stack Overflow: Stack is full."
        
        self.top += 1
        self.stack[self.top] = x
        
        # Calculate current minimum for this specific depth level
        if self.top == 0:
            self.min_stack[self.top] = x
        else:
            prev_min = self.min_stack[self.top - 1]
            self.min_stack[self.top] = x if x < prev_min else prev_min
        return None

    def pop(self):
        """Remove and return the element at the top. Time Complexity: O(1)"""
        if self.is_empty():
            return "Stack Underflow: Stack is empty."
        
        element = self.stack[self.top]
        
        # Clean up memory slots at current pointer index
        self.stack[self.top] = None
        self.min_stack[self.top] = None
        
        self.top -= 1
        return element

    def peek(self):
        """View the top element without removing it. Time Complexity: O(1)"""
        if self.is_empty():
            return "Stack Underflow: Stack is empty."
        return self.stack[self.top]

    def get_min(self):
        """Retrieve the minimum element instantly. Time Complexity: O(1)"""
        if self.is_empty():
            return "Stack is empty: No minimum element."
        return self.min_stack[self.top]

    def size(self) -> int:
        """Return total active elements in the stack. Time Complexity: O(1)"""
        return self.top + 1