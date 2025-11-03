from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.dataHolder: list[T] = []

    def push(self, new_value: T):
        """Pushes an item on top of the stack."""
        self.dataHolder.append(new_value)

    def isEmpty(self) -> bool:
        return len(self.dataHolder) == 0

    def pop(self) -> T:
        """Removes and returns the element on top of the stack"""
        if self.isEmpty():
            raise IndexError("Cannot pop an empty stack")
        return self.dataHolder.pop()

    def peek(self) -> T | None:
        """Returns the top element without removing it from the stack."""
        if self.isEmpty():
            return None
        return self.dataHolder[-1]

    def getSize(self):
        return len(self.dataHolder)

    def __str__(self):
        if self.isEmpty():
            return "Stack is empty"
        representation = "--- Top ---\n"
        for item in reversed(self.dataHolder):
            representation += f"| {item}\n"
        representation += "--- Bottom ---"

        return representation
