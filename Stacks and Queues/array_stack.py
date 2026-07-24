class ArrayStack:
    def __init__(self, capacity:int):
        self.top = -1
        self.capacity = capacity
        self.stack = []
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, x):
        if self.is_full():
            return ("Stack Overflow: Stack is full.")
        self.top = self.top + 1
        self.stack[self.top] = x

        def pop(self):
            if self.is_empty():
                return ("Stack Underflow: Stack is empty.")
            x = self.stack[self.top]
            self.top = self.top - 1
            return x

        def peek(self):
            if self.is_empty():
                return ("Stack Underflow: Stack is empty.")
            x = self.stack[self.top]
            return x

        def size(self):
            if self.is_empty():
                return ("Stack Underflow: Stack is empty.")
            if self.is_full():
                return self.capacity
            return self.top + 1

        
            


