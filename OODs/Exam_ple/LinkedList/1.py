class LinkedList:
    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = last = head
            tail = head.next
            self.size = 1
            while tail != None:
                last = tail
                tail = tail.next
                self.size += 1
            self.tail = last

    def __str__(self):
        if self.isEmpty():
            return "List is empty"

        ret = []
        tail = self.head
        while tail != None:
            ret.append(str(tail.value))
            tail = tail.next
        return "->".join(ret)

    def append(self, element):
        if type(element) != ListNode:
            node = ListNode(element)
        else:
            node = element

        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, index, element):
        if index > self.size or index < 0:
            return -1

        if type(element) != ListNode:
            node = ListNode(element)
        else:
            node = element

        if self.head == None:
            self.head = self.tail = node
        else:
            if index == 0:
                node.next = self.head
                self.head = node
            else:
                insert = self.head
                while index > 1:
                    insert = insert.next
                    index -= 1
                node.next = insert.next
                insert.next = node

        self.size += 1
        return 0

    def isEmpty(self):
        return self.size == 0

class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

        

