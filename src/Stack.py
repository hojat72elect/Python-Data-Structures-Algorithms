class Stack:
    def __init__(self):
        self.dataHolder = []

    def push(self, new_value):
        """Pushes an item on top of the stack."""
        self.dataHolder.append(new_value)

    def isEmpty(self):
        return len(self.dataHolder) == 0

    def pop(self):
        """Removes and returns the element on top of the stack"""
        if self.isEmpty():
            raise IndexError("Cannot pop an empty stack")

        return self.dataHolder.pop()

    def peek(self):
        """Returns the top element without removing it from the stack."""
        if self.isEmpty():
            raise IndexError("Cannot peek into an empty stack")

        return self.dataHolder[-1]

    def size(self):
        return len(self.dataHolder)

    def __str__(self):
        return str(self.dataHolder)
