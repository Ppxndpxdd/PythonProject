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


def have_friend(id):
    for i in range(len(lst_tuple_q)):
        if lst_tuple_q[i][0] == employee[id]:
            return i
    return -1

lst_tuple_q = [] # list that store tuple that store (department, Queue)
employee, instruction = input("Enter Input : ").split('/')
employee, instruction = (employee.split(','), instruction.split(','))
employee = dict([[int(j) for j in i.split()[::-1]] for i in employee])

for i in instruction:
    i = i.split()
    if i[0] == 'E':
        id = int(i[1])
        index = have_friend(id) 
        if index != -1:
            lst_tuple_q[index][1].enQueue(id)
        else:
            lst_tuple_q.append((employee[id], Queue([id])))            

    elif i[0] == 'D':
        if not lst_tuple_q:
            print("Empty")
            continue
        print(lst_tuple_q[0][1].deQueue())
        if lst_tuple_q[0][1].isEmpty():
            lst_tuple_q.pop(0)
