class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)
        self.size += 1
        
    def __getitem__(self, position):
        counter = 0
        if position < self.size: 
            cur = self.head
            while counter != position:
                cur = cur.next
                counter += 1
            return cur.data
        else:
            raise ValueError("position is outside of the list")
        


if __name__ == '__main__':
    listing = LinkedList()
    import code
    code.interact(local=locals())
