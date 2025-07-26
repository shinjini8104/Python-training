class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_data(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end='-->')
            temp = temp.next
        print("None")

    def delete(self, a):
        if self.head is None:
            print("delete not possible")
            return
        if a == 1:
            self.head = self.head.next
        else:
            temp = self.head
            for i in range(a - 2):
                if temp is None or temp.next is None:
                    print("position out of range")
                    return
                temp = temp.next
            if temp.next is None:
                print("position out of range")
                return
            temp.next = temp.next.next


l = LinkedList()
l.add_data(20)
l.add_data(10)
l.add_data(25)
l.add_data(28)

l.delete(12)
l.display()
