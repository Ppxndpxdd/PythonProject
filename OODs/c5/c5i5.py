class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = None
    tail = None
    for i in l:
        if head == None:
            head = node(i)
            tail = head
        else:
            tail.next = node(i)
            tail = tail.next
    return head
        
def printList(H):
    current = H
    while current is not None:
        print(current,"",end="")
        current = current.next
    print()
        
def mergeOrderesList(p,q):
    head = None
    tail = None
    def append(n):
        nonlocal head,tail
        if head == None:
            head = n
            tail = head
        else:
            tail.next = n
            tail = tail.next 
        return n.next
    while p is not None or q is not None:
        if p is not None and (q is None or p.data <= q.data):
            p = append(p)
        else:
            q = append(q)
    return head

#################### FIX comand ####################   
# input only a number save in L1,L2
L1,L2 = input("Enter 2 Lists : ").split()
L1 = list(map(int,L1.split(",")))
L2 = list(map(int,L2.split(",")))
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)