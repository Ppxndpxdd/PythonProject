class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else :
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
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
            return  " ".join(self.items)
qn = Queue()
qs = Queue()
inp = input("Enter Input : ").split(",")
if not inp == qn.isEmpty():
    for i in inp :
        i = i.split()
        if i[0]=='EN':
            qn.enQueue(i[1])

        elif i[0]=='ES':
            qs.enQueue(i[1])
            
        elif i[0]=='D': 
            if not qs.isEmpty():
                print(qs.deQueue())
                continue
            if qn.isEmpty():
                print("Empty")
                continue
            print(qn.deQueue())
else : print("input is empty")
            