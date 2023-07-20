class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            last_node = self.head

            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next

            last_node.next = node

    def insert_head(self, node):
        head_node = self.head
        self.head = node
        self.head.next = head_node
        del head_node

    def get_list(self):
        target_node = self.head
        while True:
            if target_node is None:
                print("List is empty")
                break
            print(target_node.data)
            target_node = target_node.next


n1 = Node("Bir")
n2 = Node("Ikki")
n3 = Node("Uch")
n4 = Node("Nol")

ll = LinkedList()
ll.insert(n1)
ll.insert(n2)
ll.insert(n3)

ll.get_list()

ll.insert_head(n4)
ll.get_list()