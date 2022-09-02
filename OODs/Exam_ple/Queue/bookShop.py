class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, item):
        self.items.append(item)

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
            return ", ".join(self.items)

# lst,cmd = input("Enter input : ").split("/") # auto arrange to index array

inp = input("Enter Input : ")
lst = inp.split("/")[0]
cmd = inp.split("/")[1]

book = Queue(lst.split())

for mode in cmd.split(","):
    if mode == "D":
        book.deQueue()
    else:  # E = enqueue
        book.enQueue(mode.split()[1])

checkList = []
is_duplicate = False

for check in book.items:
    if check in checkList:
        is_duplicate = True
        break
    else:
        checkList.append(check)

if is_duplicate is True:
    print("Duplicate")
else:
    print("No Duplicate")