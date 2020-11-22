class LinkedList:

    def __init__(self):
        self.head = None

    def First(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def After(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def End(self,data):

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def deleteNode(self, position):

        if self.head == None:
            return

        tem_node = self.head

        if position == 0:
            self.head = tem_node.next
            tem_node = None
            return

        for i in range(position - 1):
            tem_node = tem_node.next
            if tem_node is None:
                break

        if key is not present:
            if tem_node is None:
             return

        if tem_node.next is None:
            return

        next = tem_node.next.next
        tem_node.next = None
        tem_node.next = next

    def printList(self):
        tem_node = self.head
        while (tem_node):
            print(str(tem_node.item))
            tem_node = tem_node.next

x = LinkedList()
x.End(1)
x.First(2)
x.End(4)
x.After(a.head.next, 5)
x.deleteNode(3)
x.printList()
