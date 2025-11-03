class Queue:
    """This is a one-way queue, info comes in from one side and exits from the other side."""
    def __init__(self):
        self.dataHolder = []

    def isEmpty(self):
        return len(self.dataHolder) == 0

    def getSize(self):
        return len(self.dataHolder)

    def enqueue(self, new_value):
        self.dataHolder.append(new_value)

    def dequeue(self):
        """Removes and returns the value from front of the queue"""
        if self.isEmpty():
            raise IndexError("Cannot Dequeue an empty queue")
        return self.dataHolder.pop(0)

    def peekFront(self):
        """Returns the current item in front of the queue, without removing it"""
        if self.isEmpty():
            return None
        return self.dataHolder[0]

    def peekRear(self):
        """Returns the current item at the end of the queue, without removing it"""
        if self.isEmpty():
            return None
        return self.dataHolder[-1]