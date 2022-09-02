class Queue:
    def __init__(self, lst = None):
        self.items = [] if lst is None else lst
    
    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return not self.items

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self, lst = None):
        self.items = [] if lst is None else lst

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


normal, mirror = input("Enter Input (Normal, Mirror) : ").split()
