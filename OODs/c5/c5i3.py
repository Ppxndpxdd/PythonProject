class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    # def __str__(self):
    #     if self.size == 0:
    #         return "Empty"
    #     ret = []
    #     tail = self.head
    #     while tail != None:
    #         ret.append(str(tail.value))
    #         tail = tail.next
    #     return "".join(ret)


def createList(raw_list):
    head = ListNode(raw_list.pop(0))
    # print(id(head.next),id(temp))
    while len(raw_list) != 0:
        temp = ListNode(raw_list.pop(0))
        head.next = temp
        
    # while True

        # temp = temp.next
    return head

    # node = head
    # while True:
    #     node.value = raw_list.pop(0)
    #     if len(raw_list) == 0:
    #         break
    #     node.next = ListNode()
    #     node = node.next
    # return head


def printList(LL):
    print(LL.data)
    print(LL.next.data)
    print(LL.next.next)
    # ret = []
    # tail = head
    # while tail != None:
    #     ret.append(str(tail.value))
    #     tail = tail.next
    # return " ".join(ret)

def size(head):
    size = 0
    node = head
    while node != None:
        node = node.next
        size += 1
    return size

def mergeOrderesList(p, q):
    for i in range():
        pass
        



#################### FIX comand ####################
# input only a number save in L1,L2
L1, L2 = input("Enter 2 Lists : ").split(" ")
L1 = L1.split(",")
L2 = L2.split(",")

LL1 = createList(L1)
# LL2 = createList(L2)
printList(LL1)
# print('LL1 : ', end='')
# printList(LL1)
# print('LL2 : ', end='')
# printList(LL2)
# m = mergeOrderesList(LL1, LL2)
# print('Merge Result : ', end='')
# printList(m)
