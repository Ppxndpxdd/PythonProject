class Stack:

    """class Stack
        default : empty stack / Stack([...])
    """
    total = 0

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)
        Stack.total += 1

    def __str__(self):
        s = 'stack of'+str(self.size())+'items'
        for ele in self.items:
            s += str(ele)+''
        return s

    def push(self,i):
        self.items.append(i)
        self.size += 1

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(), "Data in stack : ", s.items)

while not s.isEmpty():

    s.pop()

print(s.size(), "Data in stack : ", s.items)