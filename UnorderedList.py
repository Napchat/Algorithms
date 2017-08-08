from Node import Node

class UnorderedList():
    '''The unordered list will be built from a collection of nodes,
    each linked to the next by explicit references, the list class 
    itself does not contain any node objects.
    '''
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()

        return False

    def remove(self, item):
        if not self.search(item):
            raise ValueError
        current = self.head
        temp = None
        while current != None:
            if current.get_data() == item:
                if temp == None:
                    self.head = current.get_next()
                else:
                    temp.set_next(current.get_next())
                break
            temp = current
            current = current.get_next()

    def append(self, item):
        new_item = Node(item)
        current = self.head
        if current != None:
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_item)
        else:
            self.head = new_item

    def index(self, item):
        current = self.head
        count = 0
        while current != None:
            if current.get_data() == item:
                return count
            current = current.get_next()
            count += 1
        raise ValueError

    def insert(self, pos, item):
        if pos >= self.size():
            raise ValueError
        new_item = Node(item)
        current = self.head
        previous = None
        while pos > 0:
            previous = current
            current = current.get_next()
            pos -= 1
        previous.set_next(new_item)
        new_item.set_next(current)

    def pop(self):
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        self.remove(current.get_data())
        return current.get_data()

    def pop(self, pos=-1):
        if pos >= self.size():
            raise ValueError
        if pos == -1:
            pos = self.size() - 1
        current = self.head
        while pos > 0:
            current = current.get_next()
            pos -= 1
        self.remove(current.get_data())
        return current.get_data()