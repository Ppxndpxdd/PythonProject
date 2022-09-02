class Queue:
    def init(self,lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = lst
    def enQueue(self,s):
        self.items.append(s)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        else:
            return "".join(self)

lst = input("Enter Input : ").split(",")
q = Queue()
for x in lst:
    if x[:2] == 'ES':
        print(x[2:])
        # if q.items[-1]:
    # elif x[0] == 'EN'
    #     if 