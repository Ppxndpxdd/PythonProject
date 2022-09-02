class Stack:

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, s):
        self.items.append(s)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


inp = input('Enter Input : ').split()

S = Stack()
c = None

for i in inp:
    if S.size() < 2:
        S.push(i)
        print(i)
    elif S.peak() == i:
        c = S.pop()
        S.peak()


print(S.size())

### Enter Your Code Here ###
