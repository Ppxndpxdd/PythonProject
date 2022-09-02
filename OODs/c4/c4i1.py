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
            return  ", ".join(self.items)

q = Queue()
q1 = Queue()
inp = input("Enter Input : ").split(",")

if not inp == q.isEmpty():
    for i in inp :
        i = i.split()
        if i[0]=='E':
            q.enQueue(i[1])
            print(q)

        elif i[0]=='D':

            if not q.isEmpty():
                out = q.deQueue()
                q1.enQueue(out)
                print(out + " <- " + str(q))
            else :
                print("Empty")
        
        else :
            print("input is incorrect")

    print(str(q1) + " : " + str(q))
else :
    print("input is empty")