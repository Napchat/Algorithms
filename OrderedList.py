from Node import Node

class OrderedList():
    '''The unordered list will be built from a collection of nodes,
    each linked to the next by explicit references, the list class 
    itself does not contain any node objects.
    '''
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def add(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        while current != None and current.get_data() < item:
            previous = current
            current = current.get_next()
        if previous == None:
            self.head = temp
            temp.set_next(current)
        else:
            previous.set_next(temp)

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            if current.get_data() > item:
                return False
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

    def index(self, item):
        current = self.head
        count = 0
        while current != None:
            if current.get_data() == item:
                return count
            current = current.get_next()
            count += 1
        raise ValueError

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